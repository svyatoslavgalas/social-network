from django.db import models

from account.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Пользователь')
    name = models.CharField('Название', max_length=256)
    pub_date = models.DateField('Дата публикации', auto_now=True)
    content = models.TextField('Контет')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.name

    @property
    def likes_count(self):
        return self.likes.count()

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ('-pub_date',)
