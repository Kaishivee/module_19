from django.contrib import admin
from .models import Game, Buyer

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'description', 'age_limited')
    search_fields = ('title',)
    list_filter = ('age_limited', 'cost',)
    fieldsets = (
        ('Информация об игре', {'fields': (('age_limited', 'title'), ('cost', 'size'))}),
        ('Дополнительное', {'fields': ('description',)}),
    )

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    list_filter = ('name',)
    search_fields = ('name',)
    fieldsets = (
        ('Информация о покупателе', {'fields': (('name',), ('balance', 'age'))}),
        ('Дополнительное', {'fields': ()}),
    )

