from django.shortcuts import render

from .forms import CommentForm
from .models import Comment, Recipe, IngredientImage, Ingredient
from .models import RecipeVideo 


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
    comments = Comment.objects.filter(recipe=recipe)

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
                        "comments": comments,
                        "form": form
                        }
            return render(request, 'recipe_detail.html', context)

        else:
            context = {
                        "recipe": recipe,
                        "comments": comments,
                        "form": form
                       }
            return render(request, 'recipe_detail.html', context)
    else:
        context = {
                    "recipe": recipe,
                    "comments": comments,
                    "form": form
                    }
        return render(request, 'recipe_detail.html', context)
