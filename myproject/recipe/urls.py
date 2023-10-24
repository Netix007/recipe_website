from django.urls import path
from .views import recipe_form, recipe_full

urlpatterns = [
    path('', recipe_form, name='recipe_add_form'),
    path('recipe/<int:recipe_id>/', recipe_full, name='recipe_full'),
]
