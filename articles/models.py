from django.db import models
from core.mixins import TranslatableField


class Author(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    about = TranslatableField(models.TextField, null=True)
    about_short = TranslatableField(models.CharField, max_length=200, null=True)

    def get_about(self, language_code):
        about_field = f'about_{language_code}'
        return getattr(self, about_field, getattr(self, 'about_en', ''))


class Article(models.Model):
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    title = TranslatableField(models.CharField, max_length=200, null=True, blank=True)
    content = TranslatableField(models.TextField, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title.get('en', 'Untitled')

    def get_title(self, language_code):
        title_field = f'title_{language_code}'
        return getattr(self, title_field, getattr(self, 'title_en', ''))

    def get_content(self, language_code):
        content_field = f'content_{language_code}'
        return getattr(self, content_field, getattr(self, 'content_en', ''))
