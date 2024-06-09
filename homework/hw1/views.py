import logging
from django.shortcuts import render


logger = logging.getLogger(__name__)


def index(request):
    context = {
        "title": "Главная страница",
        "content": "Приветствую на главной странцие",
    }
    logger.info("Index page accessed")
    return render(request, "hw1/index.html", context)


def about(request):
    context = {
        "title": "О себе",
    }
    logger.info("About page accessed")
    return render(request, "hw1/about.html", context)
