from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("orders/<int:client_id>", views.orders, name="orders"),
    path("orders/", views.orders, name="all_orders"),
    path(
        "add_client/", views.add_client, name="add_client"
    ),  # адрес для создания нового клиента
    path(
        "add_product/", views.add_product, name="add_product"
    ),  # адрес для создания нового товара
    path(
        "add_order/", views.add_order, name="add_order"
    ),  # адрес для создания нового заказа
]
