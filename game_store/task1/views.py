from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Game


def main_page(request):
    title = 'Главная страница'
    text1 = 'Главная'
    text2 = 'Магазин'
    text3 = 'Корзина'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
        'text3': text3
    }
    return render(request, 'first_task/platform.html', context)


def games_list(request):
    title = 'Игры'
    games = Game.objects.all()  # Получаем все записи из Game
    context = {
        'title': title,
        'games': games
    }
    return render(request, 'first_task/games.html', context)


def show_cart(request):
    title = 'Корзина'
    empty_cart = 'Извините, Ваша корзина пуста'
    back_home = 'Вернуться обратно'
    context = {
        'title': title,
        'empty_cart': empty_cart,
        'back_home': back_home,
    }
    return render(request, 'first_task/cart.html', context)


########################################################################################


from .forms import UserRegister
from .models import Buyer

users = ['user1', 'user2', 'user3']  # Псевдо-список пользователей


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        try:
            age = int(age)
        except ValueError:
            info['error'] = 'Некорректный возраст'
        else:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                # Проверка существования пользователя в базе данных
                user_exists = Buyer.objects.filter(name=username).exists()

                if user_exists:
                    info['error'] = 'Пользователь уже существует'
                else:
                    # Создание нового пользователя
                    new_buyer = Buyer.objects.create(
                        name=username,
                        balance=0,
                        age=age
                    )
                    info['message'] = f'Приветствуем, {username}!'

    return render(request, 'first_task/registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        try:
            age = int(age)
        except ValueError:
            info['error'] = 'Некорректный возраст'
        else:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                # Проверка существования пользователя в базе данных
                user_exists = Buyer.objects.filter(name=username).exists()

                if user_exists:
                    info['error'] = 'Пользователь уже существует'
                else:
                    # Создание нового пользователя
                    new_buyer = Buyer.objects.create(
                        name=username,
                        balance=0,
                        age=age
                    )
                    info['message'] = f'Приветствуем, {username}!'

    return render(request, 'first_task/registration_page.html', info)
