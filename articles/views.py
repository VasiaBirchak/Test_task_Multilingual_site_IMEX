from django.shortcuts import render
from .models import Article, Author
from django.utils.translation import get_language


def home(request):
    language_code = get_language()
    title_field = f'title_{language_code}'
    articles = Article.objects.all().order_by(title_field)
    for article in articles:
        article.title = article.get_title(language_code)
        article.content = article.get_content(language_code)
    return render(request, 'home.html', {'articles': articles})


def authors(request):
    authors = Author.objects.all().order_by('name')
    return render(request, 'articles/authors.html', {'authors': authors})


def article_detail(request, slug):
    language_code = get_language()
    article = Article.objects.get(slug=slug)
    article.title_localized = article.get_title(language_code)
    article.content_localized = article.get_content(language_code)
    article.author.about_localized = article.author.get_about(language_code)
    return render(request, 'articles/article_detail.html', {'article': article})


def author_detail(request, pk):
    language_code = get_language()
    author = Author.objects.get(pk=pk)
    author.about_localized = author.get_about(language_code)
    articles = author.articles.all()
    for article in articles:
        article.title_localized = article.get_title(language_code)
        print(article.title_localized)
    return render(request, 'articles/author_detail.html', {
        'author': author,
        'articles': articles,
    })
