"""Defines URL patterns for learning_logs."""
"""Определяет схемы URL  для learning_logs."""


from django.urls import path
from . import views
app_name = 'learning_logs'

urlpatterns = [
    # Home page.
    # Домашняя страница.
    path('', views.index, name='index'),

    # Page that shows all topics.
    # Страница со списком всех тем.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    # Страница с подробной информацией по отдельной теме.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic.
    # Страница для создания новой темы.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry.
    # Страница для добавления новой записи.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editting an entry.
    # Страница для редактирования записи.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]
