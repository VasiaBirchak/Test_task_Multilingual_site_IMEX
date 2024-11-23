

class TranslatableField:
    """
    Міксін для створення мультиязичних полів.
    """
    def __init__(self, field_class, **kwargs):
        """
        Ініціалізація поля. Ми зберігаємо клас поля та всі параметри для цього поля.
        """
        self.field_class = field_class
        self.kwargs = kwargs

    def contribute_to_class(self, cls, name):
        """
        Додаємо переклади для кожної мови до класу (моделі).
        """
        languages = ['en', 'uk', 'fr', 'de']  # Список доступних мов
        # Додаємо поле для кожної мови
        for lang in languages:
            field_name = f"{name}_{lang}"
            field = self.field_class(**self.kwargs)  # Створення конкретного поля
            field.contribute_to_class(cls, field_name)
        field = self.field_class(**self.kwargs)  # Створення основного поля
        field.contribute_to_class(cls, name)
