from django.contrib import admin

from .models import Subscriptions, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email',)
    search_fields = ('username', 'email',)
    list_filter = ('username', 'email',)
    ordering = ('username',)
    empty_value_display = '-пусто-'


@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('author', 'user',)
    search_fields = ('author__username', 'user__username',)
    list_filter = ('author__username', 'user__username',)
    empty_value_display = '-пусто-'
