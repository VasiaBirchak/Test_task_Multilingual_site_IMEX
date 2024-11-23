from django.contrib import admin
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Language, Author, Article


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'is_active')
    list_editable = ('is_active',)

    def has_delete_permission(self, request, obj=None):
        """
        Prevents the removal of English (or other base language).
        """
        if obj and obj.code == 'en':
            return False
        return super().has_delete_permission(request, obj)


@receiver(post_delete, sender=Language)
def delete_related_translations(sender, instance, **kwargs):
    """
    Deletes all entries associated with the deleted language.
    """
    language_code = instance.code
    Author.objects.update(**{
        f'about_{language_code}': None,
        f'about_short_{language_code}': None
    })
    Article.objects.update(**{
        f'title_{language_code}': None,
        f'content_{language_code}': None
    })
