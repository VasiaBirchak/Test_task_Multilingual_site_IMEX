from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleListAPIView.as_view(), name='article-list'),
    path('authors/', views.AuthorListAPIView.as_view(), name='author-list'),
]
