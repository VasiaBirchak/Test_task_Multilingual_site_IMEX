from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.authors, name='authors'),
    path('article/<slug:slug>/', views.article_detail, name='article-detail'),
    path('author/<int:pk>/', views.author_detail, name='author-detail'),
]
