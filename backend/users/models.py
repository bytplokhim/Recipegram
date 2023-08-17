from django.contrib.auth.models import AbstractUser
from django.db import models

from foodgram.settings import MAX_LENGHT_EMAIL, MAX_LENGHT_USER


class User(AbstractUser):
    email = models.EmailField(
        'Эл.почта', max_length=MAX_LENGHT_EMAIL, unique=True)
    first_name = models.CharField(
        'Имя', max_length=MAX_LENGHT_USER, blank=False)
    last_name = models.CharField(
        'Фамилия', max_length=MAX_LENGHT_USER, blank=False)
    username = models.CharField(
        'Логин', max_length=MAX_LENGHT_USER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username


class Subscriptions(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        related_name='follower',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        related_name='author',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='Уникальность подписки.'
            ),
            models.CheckConstraint(
                check=~models.Q(author=models.F('user')),
                name='Подписка на себя.'
            ),
        ]

    def __str__(self):
        return f'{self.user} подписался на рецепты {self.author}'
