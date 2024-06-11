import random
from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        for i in range(1, 5):
            client = Client.objects.get(id=i)
            products = []
            products = [Product.objects.get(id=random.randint(1,5)) for _ in range(3)]
            order = Order.objects.create(buyer=client)
            order.order.add(*products)
            order.calculate_total()
            order.save()

        self.stdout.write(self.style.SUCCESS("Fake orders is added"))


