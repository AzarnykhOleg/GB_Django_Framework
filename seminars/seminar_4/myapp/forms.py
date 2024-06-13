import datetime
from django import forms
from .models import Author


class GameForm(forms.Form):
    EVENT_CHOICE = [("coin", "Монетка"), ("dice", "Кости"), ("number", "Числа")]
    event_type = forms.ChoiceField(choices=EVENT_CHOICE, label="Выберите игру")
    attempts = forms.IntegerField(min_value=1, max_value=64, label="Количество попыток")


class AuthorForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea)
    birthday = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )


class ArticleForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    pub_date = forms.DateField(
        initial=datetime.date.today, attrs={"class": "form-control", "type": "date"}
    )
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField()
    views = forms.IntegerField(initial=0)
    is_published = forms.BooleanField(initial=False)
