import datetime
import random
from django.core.management.base import BaseCommand
from myapp.models import Article, Author, Comment



class Command(BaseCommand):
    help = "Create comments."

    def add_arguments(self, parser):
        parser.add_argument(
            "count", type=int, help="count of fake authors and articles"
        )

    def handle(self, *args, **kwargs):
        count = kwargs.get("count")
        
        for i in range(1, count + 1):
            for j in range(1, count + 1):
                comment = Comment(
                    author = Author.objects.filter(id=i).first(),
                    article = Article.objects.get(id=j),
                    comment = f'Comment {i}',
                )
                comment.save()
