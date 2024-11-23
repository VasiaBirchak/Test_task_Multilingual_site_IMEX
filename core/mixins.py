

class TranslatableField:
    def __init__(self, field_class, **kwargs):
        self.field_class = field_class
        self.kwargs = kwargs

    def contribute_to_class(self, cls, name):
        languages = ['en', 'uk', 'fr', 'de']
        for lang in languages:
            field_name = f"{name}_{lang}"
            field = self.field_class(**self.kwargs)
            field.contribute_to_class(cls, field_name)
        field = self.field_class(**self.kwargs)
        field.contribute_to_class(cls, name)
