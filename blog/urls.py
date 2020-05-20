from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_index, name='home'),
    path("recipe/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("ingredient/<int:recipe_pk>/<int:pk>/", views.ingredient_detail, name="ingredient_detail"),
]
