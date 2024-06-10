from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = "Get client."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument("name", type=str, help="Client name", default=None)
        parser.add_argument("email", type=str, help="Client email", default=None)

    def handle(self, *args, **kwargs):
        pk = kwargs.get("pk")
        name = kwargs.get("name")
        email = kwargs.get("email")
        client = Client.objects.filter(pk=pk).first()
        if name is not None:
            client.name = name
        if email is not None:
            client.email = email
        client.save()
        # self.stdout.write(f"Client id={pk} is updated")
        self.stdout.write(self.style.SUCCESS(f"Client id={pk} is updated"))
