from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(
            name="Andrey",
            email="example@mail.com",
            phone="+7(111)-222-33-33",
            address="MSC",
        )
        client.save()
        self.stdout.write(self.style.SUCCESS(f"Client:'{client}' is registered"))
