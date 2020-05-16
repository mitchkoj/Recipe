from django.db import models
from account.models import CustomUser


class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='static/img/', blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.recipe_id} - {self.title}"


class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True, unique=True)
    ingredient_name = models.CharField(max_length=250, blank=False, null=False)
    ingredient_direction = models.CharField(max_length=300)
    purchase_store = models.CharField(max_length=250)
    purchase_location = models.CharField(max_length=250)
    pricing = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ingredient_id} - {self.ingredient_name}"


class IngredientImage(models.Model):
    image = models.ImageField(upload_to='static/img/', blank=True, null=True)
    recipe = models.ForeignKey('Ingredient', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.recipe}"

class RecipeVideo(models.Model):
    video = models.FileField(upload_to='static/videos/', null=True, blank=True)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe}"

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
