import pytest
from articles.models import Author, Article


@pytest.mark.django_db
def test_author_model_creation():
    author = Author.objects.create(
        name="John Doe",
        birthday="1980-01-01",
        about_en="About John in English",
        about_uk="Про Джона українською"
    )
    assert author.name == "John Doe"
    assert author.birthday == "1980-01-01"
    assert author.about_en == "About John in English"
    assert author.about_uk == "Про Джона українською"


@pytest.mark.django_db
def test_article_model_creation():
    author = Author.objects.create(
        name="John Doe",
        birthday="1980-01-01",
        about_en="About John in English",
        about_uk="Про Джона українською"
    )
    article = Article.objects.create(
        slug="test-article",
        title_en="Test Article",
        title_uk="Тестова стаття",
        content_en="Test content in English",
        content_uk="Тестовий контент українською",
        author=author
    )
    assert article.slug == "test-article"
    assert article.title_en == "Test Article"
    assert article.title_uk == "Тестова стаття"
    assert article.content_en == "Test content in English"
    assert article.content_uk == "Тестовий контент українською"
