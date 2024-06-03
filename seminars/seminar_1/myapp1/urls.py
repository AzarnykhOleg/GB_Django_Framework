from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("coin/", views.flip_coin, name='coin'),
    path("cube/", views.roll_cube, name='cube'),
    path("number/", views.random_number, name='number'),
]