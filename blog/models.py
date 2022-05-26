from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

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

class Comment(models.Model):
    """ Комментарии и оценки к статьям """
    class Ratings(models.IntegerChoices):  # https://docs.djangoproject.com/en/4.0/ref/models/fields/#enumeration-types
        WITHOUT_RATING = 0, _('Без оценки')
        TERRIBLE = 1, _('Ужасно')
        BADLY = 2, _('Плохо')
        FINE = 3, _('Нормально')
        GOOD = 4, _('Хорошо')
        EXCELLENT = 5, _('Отлично')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/#many-to-one-relationships
    note = models.ForeignKey(Note, on_delete=models.CASCADE,
                             related_name='comments')  # default related_name='comment_set'
    rating = models.IntegerField(default=Ratings.WITHOUT_RATING, choices=Ratings.choices,
                                 verbose_name='Оценка')

    def __str__(self):
        # https://django.fun/docs/django/ru/3.1/ref/models/instances/#django.db.models.Model.get_FOO_display
        return f'{self.get_rating_display()}: {self.author}'

