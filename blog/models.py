from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField('Заголовок', max_length=60)
    message = models.TextField('Текст статьи')
    public = models.BooleanField('Опубликовать')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

