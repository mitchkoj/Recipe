from django.shortcuts import render

from .forms import CommentForm
from .models import Comment, Recipe, IngredientImage, Ingredient
from .models import RecipeVideo, RecipeInstructions


def render_index(request):
    """
        An index view that shows a snippet of information
        about each project.
    """

    # get all project objects in the database
    recipes = Recipe.objects.all()

    # dictionary argument for render engine
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def recipe_detail(request, pk):
    """
        An detail view that shows more information
        on a particular topic.

        takes a project id.
    """

    # get the project with primary key
    recipe = Recipe.objects.get(pk=pk)
    ingredients = Ingredient.objects.filter(recipe=recipe)
    instructions = RecipeInstructions.objects.filter(recipe=recipe)
    #images = IngredientImage.objects.filter(ingredient=ingredient)
    comments = Comment.objects.filter(recipe=recipe)
    video = RecipeVideo.objects.filter(recipe=recipe)[0]

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                recipe=recipe
            )
            comment.save()

            form = CommentForm()
            context = {
                        "recipe": recipe,
                        "ingredients": ingredients,
                        "instructions": instructions,
                        "comments": comments,
                        "video": video,
                        "form": form
                        }
            return render(request, 'recipe_details.html', context)

        else:
            context = {
                        "recipe": recipe,
                        "ingredients": ingredients,
                        "instructions": instructions,
                        "comments": comments,
                        "video": video,
                        "form": form
                       }
            return render(request, 'recipe_details.html', context)
    else:
        context = {
                    "recipe": recipe,
                    "ingredients": ingredients,
                    "instructions": instructions,
                    "comments": comments,
                    "video": video,
                    "form": form
                    }
        return render(request, 'recipe_details.html', context)
