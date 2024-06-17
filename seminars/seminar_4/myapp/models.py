from django.db import models


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

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

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


class FlipCoin(models.Model):
    FLIP_CHOICES = [("heads", "Орел"), ("tails", "Решка")]

    result = models.CharField(max_length=5, choices=FLIP_CHOICES)
    flip_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.result} flipped at {self.flip_time}"

    @staticmethod
    def get_last_n_flips_stats(n):
        flips = FlipCoin.objects.order_by("-flip_time")[:n]
        stats = {"heads": 0, "tails": 0}
        for flip in flips:
            if flip.result == "Орел":
                stats["heads"] += 1
            else:
                stats["tails"] += 1
        return stats
