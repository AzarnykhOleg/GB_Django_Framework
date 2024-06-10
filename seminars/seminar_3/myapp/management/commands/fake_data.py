import datetime
import random
from django.core.management.base import BaseCommand
from myapp.models import Article, Author



class Command(BaseCommand):
    help = "Create articles and authors."

    def add_arguments(self, parser):
        parser.add_argument(
            "count", type=int, help="count of fake authors and articles"
        )

    def handle(self, *args, **kwargs):
        count = kwargs.get("count")
        for i in range(1, count + 1):
            author = Author(
                name=f"Author_{i}",
                last_name=f"Lastname{i}",
                email=f"mail{i}@mail.ru",
                bio=f"Bio{i}",
                birthday=datetime.datetime.today(),
            )
            author.save()
            for j in range(1, count + 1):
                post = Article(
                    title=f"Title-{j}",
                    text=f"Sometext{j}",
                    author=author,
                    category="Some category",
                    is_published=random.choice([False, True]),
                )
                post.save()
