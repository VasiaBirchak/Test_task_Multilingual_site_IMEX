from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer
from django.db.models import Q


class ArticleListView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        articles = Article.objects.filter(
            Q(title_en__icontains=query) | Q(content_en__icontains=query)
        )
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class AuthorListView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        authors = Author.objects.filter(name__icontains=query)
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
