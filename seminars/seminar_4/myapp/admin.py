from django.contrib import admin
from .models import FlipCoin, Article, Author, Comment
from .admin_mixins import ExportAsCSVMixin


@admin.action(description="Сменить имя на None")
def reset_name(modeladmin, request, queryset):
    queryset.update(name="None")




class AuthorAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    list_display = ["name", "last_name", "email", "bio", "birthday"]
    ordering = ["-name", "birthday"]
    list_filter = ["email", "birthday"]
    search_fields = ['bio']
    search_help_text = 'Поиск по полю Биография (bio)'
    actions = [reset_name]
    actions = ['export_as_csv']
    readonly_fields = ["birthday"]
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"], # будет занимать все доступное место на странице
                "fields": ["name"],
            },
        ),
        (
            "Подробности",
            {
                "classes": ["collapse"], # скрыты по умолчанию
                "description": "Фамилия и биография автора",
                "fields": ["last_name", "bio"],
            },
        ),
        (
            "Контакты",
            {
                "fields": ["email"], # выводятся в одну строку
            },
        ),
        (
            "Рейтинг и прочее",
            {
                "description": "Дата родждения",
                "fields": ["birthday"],
            },
        ),
    ]



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'category', 'author', 'is_published']


# Register your models here.
# myModels = [FlipCoin, Article, Author, Comment]
# admin.site.register(myModels)


# admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(FlipCoin)
admin.site.register(Author, AuthorAdmin)
