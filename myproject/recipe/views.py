import logging

from django.shortcuts import render, get_object_or_404
from .forms import RecipeForm
from .models import Recipe

logger = logging.getLogger(__name__)


def recipe_full(request, recipe_id):
    post = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe/recipe_full.html', {'recipe': post})


def recipe_form(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Recipe.objects.create(
                name=form.cleaned_data.get("name"),
                description=form.cleaned_data.get("description"),
                cooking_steps=form.cleaned_data.get("cooking_steps"),
                cooking_time=form.cleaned_data.get("cooking_time"),
                image=form.cleaned_data.get("image"),
                author=form.cleaned_data.get("author"),
                ingredients=form.cleaned_data.get("ingredients")
            )
            obj.save()
            logger.info(f'Добавлен рецепт {form.cleaned_data=}.')
    else:
        form = RecipeForm()
    return render(request, 'recipe/recipe_add_form.html', {'form': form})
