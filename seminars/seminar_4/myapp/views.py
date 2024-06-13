import logging
import random
from django.shortcuts import redirect, render
from .models import Article, Author
from .forms import GameForm, AuthorForm, ArticleForm



logger = logging.getLogger(__name__)


def index(request):
    context = {
        "title": "Главная страница",
        "content": "Приветствую на главной странцие",
    }
    logger.info("Index page accessed")
    return render(request, "myapp/index.html", context)

def flip_coin(request, tryes: int):
    logger.info("Coin page accessed")
    flips_list = [random.choice(["Орёл", "Решка"]) for _ in range(tryes)]
    context = {"title": "Flip coin", "content": flips_list}
    return render(request, "myapp/games_result.html", context)


def roll_cube(request, tryes: int):
    logger.info("Cube page accessed")
    cubes_list = [random.randint(1, 6) for _ in range(tryes)]
    context = {"title": "Cube game", "content": cubes_list}
    return render(request, "myapp/games_result.html", context)


def random_number(request, tryes: int):
    logger.info("Number page accessed")
    cubes_list = [random.randint(1, 100) for _ in range(tryes)]
    context = {"title": "Random numbers", "content": cubes_list}
    return render(request, "myapp/games_result.html", context)

def games(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['event_type']
            attempts = form.cleaned_data['attempts']
            logger.info(f"game = {game}, attempts = {attempts}")
            if game == "coin":
                return flip_coin(request, attempts)
            elif game == "dice":
                return roll_cube(request, attempts)
            elif game == 'number':
                return random_number(request, attempts)
    else:
        form = GameForm()

    return render(request, 'myapp/games.html', {'form':form})

def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            Author.objects.create(
                name=form_data['name'],
                last_name=form_data['last_name'],
                email=form_data['email'],
                bio=form_data['bio'],
                birthday=form_data['birthday'],
                )
    else:
        form = AuthorForm()
    authors = Author.objects.all()
    context= {'authors': authors, 'form': form}
    return render(request, 'myapp/authors.html', context)


def articles(request, id_author: int=None):
    if id_author:
        author = Author.objects.filter(id=id_author).first()
        arts = Article.objects.filter(author=author)
        title = f"Статьи автора: {author.full_name()}"
    else:
        arts = Article.objects.all()
        title = "Все статьи"
    context = {
        "title": title,
        "artcles_list": arts,
    }
    return render(request, "myapp/articles.html", context)

def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            Article.objects.create(
                title = form_data['title'],
                text = form_data['text'],
                author = form_data['author'],
                category = form_data['category'],
                is_published = form_data['is_published'],
            )
            return redirect('articles')
    else:
        form = ArticleForm()
    context= {'title': 'Добавить статью', 'form': form}
    return render(request, 'myapp/add_article.html', context)