from django.contrib import admin
from .models import IngredientImage, RecipeVideo, Comment
from .models import Recipe, Ingredient, RecipeInstructions
# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    action_on_top = True
    actions_on_bottom = False

    fields = ('title', 'description', 'image', 'tag', 'user')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    action_on_top = True
    actions_on_bottom = False

    fields = ('ingredient_name', 'ingredient_image', 'ingredient_direction', 'purchase_store',
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


@admin.register(RecipeInstructions)
class RecipeInstructionsAdmin(admin.ModelAdmin):
    action_on_top = True
    actions_on_bottom = False

    fields = ('instruction', 'recipe')

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
