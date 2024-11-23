from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='article-list'),
    path('authorsa/', views.AuthorListView.as_view(), name='author-list'),
]
