from django.core.management.base import BaseCommand
from myapp.models import FlipCoin
import random


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        flip = FlipCoin(result=random.choice(["Орел", "Решка"]))
        flip.save()
        