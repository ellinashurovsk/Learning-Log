from django.contrib import admin
from .models import Topic, Entry

# Register your models here.
# Зарегистрируйте ваши модели здесь.
# управление моделью осуществляется через административный сайт
admin.site.register(Topic)
admin.site.register(Entry)
