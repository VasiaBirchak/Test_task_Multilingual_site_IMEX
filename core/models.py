from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=10, unique=True)  # 'en', 'uk'
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)  # Is this language available?

    def __str__(self):
        return self.name
