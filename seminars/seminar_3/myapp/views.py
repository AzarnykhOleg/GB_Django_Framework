import logging
import random
from django.shortcuts import render, get_object_or_404
from .models import Article, Author


logger = logging.getLogger(__name__)


def index(request):
    context = {
        "title": "Главная страница",
        "content": "Приветствую на главной странцие",
    }
    logger.info("Index page accessed")
    return render(request, "myapp/index.html", context)


def about(request):
    context = {
        "title": "О себе",
    }
    logger.info("About page accessed")
    return render(request, "myapp/about.html", context)


def flip_coin(request, tryes: int):
    logger.info("Coin page accessed")
    flips_list = [random.choice(["Орёл", "Решка"]) for _ in range(tryes)]
    context = {"title": "Flip coin", "content": flips_list}
    return render(request, "myapp/games.html", context)


def roll_cube(request, tryes: int):
    logger.info("Cube page accessed")
    cubes_list = [random.randint(1, 6) for _ in range(tryes)]
    context = {"title": "Cube game", "content": cubes_list}
    return render(request, "myapp/games.html", context)


def random_number(request, tryes: int):
    logger.info("Number page accessed")
    cubes_list = [random.randint(1, 100) for _ in range(tryes)]
    context = {"title": "Random numbers", "content": cubes_list}
    return render(request, "myapp/games.html", context)


def articles(request, id_author: int):
    author = Author.objects.filter(id=id_author).first()
    arts = Article.objects.filter(author=author)
    context = {
        "title": f"Статьи автора: {author.full_name()}",
        "artcles_list": arts,
    }
    return render(request, "myapp/articles.html", context)


def full_article(request, id_article: int):
    article = get_object_or_404(Article, id=id_article)
    article.add_view()
    article.save()
    context = {
        "title": "Статья",
        "article": article,
        }
    return render(request, "myapp/full_article.html", context)
