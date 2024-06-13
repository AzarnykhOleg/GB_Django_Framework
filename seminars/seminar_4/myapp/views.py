import logging
import random
from django.shortcuts import render
from .models import Author
from .forms import GameForm, AuthorForm



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
            author = Author.objects.create(
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


