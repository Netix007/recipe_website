from django.urls import path
from .views import index, recipe_form, recipe_full

urlpatterns = [
    path('', index, name='index'),
    path('add/', recipe_form, name='recipe_add_form'),
    path('recipe/<int:recipe_id>/', recipe_full, name='recipe_full'),
]
