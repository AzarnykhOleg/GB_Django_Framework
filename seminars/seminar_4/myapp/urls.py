from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.games, name='games'),
    path('author/', views.add_author, name='add_author'),
    path('add_article/', views.add_article, name='add_article'),
    path('articles/', views.articles, name='articles'),
]