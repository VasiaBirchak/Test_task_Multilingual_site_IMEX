from django.utils.translation import activate
from .models import Language


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'en')[:2]
        available_languages = Language.objects.filter(is_active=True).values_list('code', flat=True)
        if accept_language not in available_languages:
            accept_language = 'en'
        activate(accept_language)
        request.LANGUAGE_CODE = accept_language
        return self.get_response(request)
