from django.db.models import Sum

from recipes.models import RecipeIngredient


def generate_shopping_list(user):
    ingredient_list = "Список покупок:"

    ingredients = RecipeIngredient.objects.filter(
        recipe__shoppingcart__user=user
    ).values(
        'ingredient__name', 'ingredient__measurement_unit'
    ).annotate(amount=Sum('amount'))

    for num, i in enumerate(ingredients):
        ingredient_list += (
            f"\n{i['ingredient__name']} - "
            f"{i['amount']} {i['ingredient__measurement_unit']}"
        )
        if num < ingredients.count() - 1:
            ingredient_list += ', '

    return ingredient_list
