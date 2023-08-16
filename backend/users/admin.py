from django.contrib import admin

from .models import Subscriptions, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'recipe_count',
        'follower_count'
    )
    search_fields = ('username', 'email',)
    list_filter = ('username', 'email',)
    ordering = ('username',)
    empty_value_display = '-пусто-'

    def recipe_count(self, user):
        return user.recipe.count()
    recipe_count.short_description = 'Количество рецептов'

    def follower_count(self, user):
        return user.follower.count()
    follower_count.short_description = 'Количество подписчков'


@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('author', 'user',)
    search_fields = ('author__username', 'user__username',)
    list_filter = ('author__username', 'user__username',)
    empty_value_display = '-пусто-'
