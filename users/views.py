from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register a new user."""
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        # Display blank registration form.
        # Выводит пустую форму регистрации.
        form = UserCreationForm()
    else:
        # Process completed form.
        # Обработка заполненной формы.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            # Выполнение входа и перенаправлкние на домашнюю страницу.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display a blank or invalid form.
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
