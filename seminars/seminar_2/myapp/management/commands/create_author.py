from django.core.management.base import BaseCommand
from myapp.models import Author



class Command(BaseCommand):
    help = "Create author."

    def handle(self, *args, **kwargs):
        author = Author(
            name='Shamil',
            last_name='Mentorov',
            email='shamil@example.com',
            bio='Text',
            birthday='2024-06-06',
        )
        author.save()
        self.stdout.write(f"Автор:'{author.full_name()}' добавлен в бд")