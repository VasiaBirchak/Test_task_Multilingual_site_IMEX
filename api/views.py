from rest_framework import generics
from articles.models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer


class ArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
