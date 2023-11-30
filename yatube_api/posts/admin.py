from django.contrib import admin

from .models import Comment, Post, Follow, Group


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Настройка раздела Публикации."""

    list_display = ('id', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Настройка раздела Сообщества."""

    list_display = ('title', 'slug', 'description')
    search_fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Настройка раздела Комментарии."""

    list_display = ('author', 'text', 'created', 'post')
    search_fields = ('text',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Настройка раздела Подписки."""

    list_display = ('following', 'user')
    search_fields = ('following',)
