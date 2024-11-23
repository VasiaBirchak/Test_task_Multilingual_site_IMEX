from django.contrib import admin
from .models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'is_active')
    list_editable = ('is_active',)
