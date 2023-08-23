from colorfield.fields import ColorField
from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from foodgram.settings import MAX_LENGHT_RECIPE

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField('Название', max_length=MAX_LENGHT_RECIPE)
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=MAX_LENGHT_RECIPE
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)
        constraints = (
            models.UniqueConstraint(
                fields=('name', 'measurement_unit'),
                name='Уникальность ингредиента.'
            ),
        )

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}.'


class Tag(models.Model):
    name = models.CharField(
        'Название',
        max_length=MAX_LENGHT_RECIPE,
        unique=True
    )
    color = ColorField('Цвет')
    slug = models.SlugField('Slug', max_length=MAX_LENGHT_RECIPE, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        related_name='recipe',
        on_delete=models.CASCADE,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингредиенты',
        related_name='ingredients',
        through='RecipeIngredient',
    )
    name = models.CharField('Название', max_length=MAX_LENGHT_RECIPE)
    image = models.ImageField(
        'Фото',
        upload_to='static/recipe/',
        blank=True
    )
    text = models.TextField('Описание')
    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления',
        validators=(
            validators.MinValueValidator(
                1, message='Время приготовления не может быть меньше 1 минуты.'
            ),
            validators.MaxValueValidator(
                1500, message='Слишком долгое время приготовления.'
            )
        )
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        related_name='tags',
        through='RecipeTag',
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('name',)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name='Ингредиент',
        on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField(
        'Количество',
        validators=(
            validators.MinValueValidator(1),
            validators.MaxValueValidator(1000)
        )
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('recipe', 'ingredient'),
                name='Уникальность ингредиента в рецепте.'
            ),
        )

    def __str__(self):
        return f'{self.recipe} -> {self.ingredient},{self.amount}.'


class RecipeTag(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        Tag,
        verbose_name='Тег',
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('recipe', 'tag'),
                name='Уникальность тега в рецепте.'
            ),
        )

    def __str__(self):
        return f'{self.recipe} -> {self.tag}'


class AbstractUserRelatedModel(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Избранный рецепт',
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True
        verbose_name = 'Абстрактная модель'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='Проверка на уникальность.'
            ),
        )


class Favorite(AbstractUserRelatedModel):

    class Meta:
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'

    def __str__(self):
        return f'{self.user} добавил в избранное {self.recipe}.'


class ShoppingCart(AbstractUserRelatedModel):

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.user} добавил в корзину {self.recipe}.'
