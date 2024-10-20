"""
URL configuration for game_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task1.views import main_page, games_list, show_cart, sign_up_by_html, sign_up_by_django
from task2.views import post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/', main_page),
    path('platform/games/', games_list),
    path('platform/cart/', show_cart),
    path('sign_up_by_html/', sign_up_by_html),
    path('sign_up_by_django/', sign_up_by_django),
    path('posts/', post_list, name='post_list')

]
