""" Определяем схемы URL для пользователей"""

from django.urls import path, include

from . import views


app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    # Включить URL авторизации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    # Страница регистрации.
    path('register/', views.register, name='register'),
]
