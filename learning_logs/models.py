from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """A topic the user is learning about."""
    """Тема, которую изучает пользователь."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        """ Возвращает строковое представление модели."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    """Информация, изученная пользователем по теме."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        """Возвращает строковое представление модели."""
        if len(self.text) <= 50:   # 18.2 task
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."
