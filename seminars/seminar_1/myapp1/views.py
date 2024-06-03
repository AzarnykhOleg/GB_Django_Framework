import logging
from django.http import HttpResponse
import random


logger = logging.getLogger(__name__)


def index(request):
    logger.info("Index page accessed")
    return HttpResponse("Hello, world!")


def about(request):
    logger.info("About page accessed")
    return HttpResponse("About Us")


def flip_coin(request):
    logger.info("Coin page accessed")
    return HttpResponse(random.choice(["Орёл", "Решка"]))


def roll_cube(request):
    logger.info("Cube page accessed")
    result = random.randint(1, 6)
    return HttpResponse(f"Выпал кубик = {result}")


def random_number(request):
    logger.info("Number page accessed")
    result = random.randint(1, 100)
    return HttpResponse(f"Случайное число от 0 до 100 = {result}")
