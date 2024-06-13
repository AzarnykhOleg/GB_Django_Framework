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
    
    def __str__(self) -> str:
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