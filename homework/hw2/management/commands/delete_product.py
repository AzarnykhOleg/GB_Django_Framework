from django.core.management.base import BaseCommand
from hw2.models import Product


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):

        for i in range(1, 6):
            product = Product(
                title=f"product{i}",
                description=f"description{i}",
                price=i * 1.1,
                quantity=i,
            )
            product.save()
        self.stdout.write(self.style.SUCCESS("Some fake products are registered"))


    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get("pk")
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
            self.stdout.write(self.style.WARNING(f"Product {product.title} is deleted"))