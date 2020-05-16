from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_index, name='home'),
    path("<int:pk>/", views.recipe_detail, name="recipe_detail"),
]
