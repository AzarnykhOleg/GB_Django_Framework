from django.core.management.base import BaseCommand
from myapp.models import Article, Author



class Command(BaseCommand):
    help = "Create article."
    
    def handle(self, *args, **kwargs):
        article = Article(
            title='First',
            text='Some text',
            author=Author.objects.filter(pk=1).first(),
            category='Some category'
            )
        article.save()
        self.stdout.write(f"Статья:'{article.title}' добавлена")