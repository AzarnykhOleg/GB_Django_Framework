from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('game_coin/<int:tryes>', views.flip_coin, name='flip_coin'),
    path('game_cube/<int:tryes>', views.roll_cube, name='cube'),
    path('game_number/<int:tryes>', views.random_number, name='numbers'),
    path('author/', views.articles, name='all_articles'),
    path('author/<int:id_author>', views.articles, name='articles'),
    path('full_article/<int:id_article>', views.full_article, name='full_article'),
    path('orders/<int:client_id>', views.orders, name='orders'),
    path('orders/', views.orders, name='all_orders'),
]