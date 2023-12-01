from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

MAX_LENGTH = 30


class Group(models.Model):
    """Модель класса Group."""

    title = models.CharField(
        'Название сообщества',
        max_length=200,
    )
    slug = models.SlugField(
        'Слаг названия сообщества',
        unique=True,
    )
    description = models.TextField(
        'Описание сообщества',
    )

    class Meta:
        verbose_name = 'сообщество'
        verbose_name_plural = 'Сообщества'

    def __str__(self):
        return self.title[:MAX_LENGTH]


class Post(models.Model):
    """Модель класса Post."""

    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE,
        related_name='posts',
    )
    text = models.TextField(
        'Текст публикации',
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        null=True,
        blank=True,
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Сообщество',
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('pub_date',)

    def __str__(self):
        return (f'{self.author.username} - {self.pub_date} - '
                f'{self.text[:MAX_LENGTH]}')


class Comment(models.Model):
    """Модель класса Comment."""

    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField(
        'Текст комментария',
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )
    post = models.ForeignKey(
        Post,
        verbose_name='Публикация',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return (f'{self.author.username} - {self.created} - '
                f'{self.post.text[:MAX_LENGTH]} - {self.text[:MAX_LENGTH]}')


class Follow(models.Model):
    """Модель класса Follow."""

    user = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
        related_name='subscriber',
    )
    following = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                name='%(app_label)s_%(class)s_unique_relationships',
                fields=['user', 'following'],
            ),
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_prevent_self_follow',
                check=~models.Q(user=models.F('following')),
            ),
        ]

    def __str__(self):
        return (f'{self.user} подписан на {self.following}')
