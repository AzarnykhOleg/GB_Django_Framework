from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin_flip/', views.coin_flip_view, name='coin_flip'),
    path('coin_flip_n/', views.coin_flip_n, name='coin_flip_n'),
]