from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Отображаемые поля в списке постов
    list_filter = ('created_at',)  # Фильтры по дате создания
    search_fields = ('title', 'content')  # Поля, по которым можно выполнять поиск
