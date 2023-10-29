from django.urls import path
from .views import index, recipe_form, recipe_full, UserRegisterView, UserLoginView, UserLogoutView, recipe_catalog

urlpatterns = [
    path('', index, name='index'),
    path('add/', recipe_form, name='recipe_add_form'),
    path('recipe/<int:recipe_id>/', recipe_full, name='recipe_full'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('catalog/', recipe_catalog, name='recipe_catalog'),
]
