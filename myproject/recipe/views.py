import logging

from django.shortcuts import render, get_object_or_404
from .forms import RecipeForm, UserRegisterForm, UserLoginForm
from .models import Recipe
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

logger = logging.getLogger(__name__)


def index(request):
    random_recipe = Recipe.objects.order_by('?')[:5]
    dict_recipe = {}
    for i in range(1, len(random_recipe)+1):
        dict_recipe[i] = random_recipe[i-1]
    return render(request, 'index.html', {'random_recipe': dict_recipe})


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


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'recipe/register.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'recipe/login.html'
    next_page = 'index'
    success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context


class UserLogoutView(LogoutView):
    next_page = 'index'
