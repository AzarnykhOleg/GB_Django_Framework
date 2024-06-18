from decimal import Decimal
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, email: {self.email}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    product_add_date = models.DateField(auto_now_add=True)
    product_image = models.ImageField(upload_to="product_images/", default=None)

    def __str__(self):
        return f"{self.title}, цена: {self.price}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    buyer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Клиент: {self.buyer}, сумма заказа = {self.total_amount}"

    def calculate_total(self):
        total = Decimal(0)
        for product in self.products.all():
            total += product.price
        self.total_amount = total
        self.save()

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
