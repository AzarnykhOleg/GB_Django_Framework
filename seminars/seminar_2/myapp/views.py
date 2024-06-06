import logging
from django.shortcuts import render
from .models import FlipCoin

logger = logging.getLogger(__name__)


def index(request):
    context = {
        "title": "Главная страница",
        "content": "Приветствую на главной странцие",
    }
    logger.info("Index page accessed")
    return render(request, "myapp/index.html", context)


def coin_flip_view(request):
    flips = FlipCoin.objects.all()
    context = {
        "title": "Главная страница",
        "flips": flips,
        }
    return render(request, 'myapp/coin_flip.html', context)


def coin_flip_n(request):
    flips = FlipCoin.get_last_n_flips_stats(5)
    context = {
        "title": "Главная страница",
        "flips": flips,
        }
    return render(request, 'myapp/coin_flip.html', context)