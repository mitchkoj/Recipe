from django.contrib import admin
from .models import Recipe, Ingredient, IngredientImage, RecipeVideo, Comment

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    action_on_top = True
    actions_on_bottom = False

    fields = ('title', 'description', 'image', 'user')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    action_on_top = True
    actions_on_bottom = False

    fields = ('ingredient_name', 'ingredient_direction', 'purchase_store',
              'purchase_location', 'pricing', 'cost', 'recipe')


@admin.register(IngredientImage)
class IngredientImageAdmin(admin.ModelAdmin):
    action_on_top = True
    actions_on_bottom = False

    fields = ('image', 'recipe')


@admin.register(RecipeVideo)
class RecipeVideoAdmin(admin.ModelAdmin):
    action_on_top = True
    actions_on_bottom = False

    fields = ('video', 'recipe')


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
