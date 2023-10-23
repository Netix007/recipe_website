from django.urls import path
from .views import recipe_form

urlpatterns = [
    path('', recipe_form, name='recipe_add_form'),
]
