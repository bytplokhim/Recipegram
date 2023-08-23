from django.contrib import admin

from .models import (Ingredient, Favorite,
                     Recipe, RecipeIngredient,
                     RecipeTag, ShoppingCart,
                     Tag)


class IngredientsInLine(admin.TabularInline):
    model = RecipeIngredient
    min_num = 1
    extra = 2


class TagsInLine(admin.TabularInline):
    model = RecipeTag
    min_num = 1
    extra = 1


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'recipe']
    search_fields = ['user__username', 'user__email']
    empty_value_display = '-пусто-'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'measurement_unit']
    search_fields = ['name']
    empty_value_display = '-пусто-'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'favorites', 'ingredients_list']
    search_fields = ['name', 'author__username']
    list_filter = ['tags']
    empty_value_display = '-пусто-'
    inlines = (IngredientsInLine, TagsInLine)

    def favorites(self, obj):
        if Favorite.objects.filter(recipe=obj).exists():
            return Favorite.objects.filter(recipe=obj).count()
        return 0

    def ingredients_list(self, obj):
        return ', '.join([
            ingredient.name for ingredient in obj.ingredients.all()])
    ingredients_list.short_description = 'Ингредиенты'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'recipe']
    search_fields = ['user__username', 'user__email']
    empty_value_display = '-пусто-'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'slug']
    search_fields = ['name', 'slug']
    empty_value_display = '-пусто-'
