from django.db import models
from decimal import Decimal


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def full_name(self):
        return f"{self.name} {self.last_name}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} author: {self.author}"

    def add_view(self):
        self.views += 1


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Name: {self.name}, email: {self.email}"


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    product_add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Title: {self.title}, price: {self.price}, quantity: {self.quantity}"


class Order(models.Model):
    buyer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Client: {self.buyer}, total amount = {self.total_amount}"

    def calculate_total(self):
        total = Decimal(0)
        for product in self.products.all():
            total += product.price
        self.total_amount = total
        self.save()
