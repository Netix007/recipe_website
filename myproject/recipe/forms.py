from django import forms


class RecipeForm(forms.Form):
    name = forms.CharField(label="Название", max_length=150)
    ingredients = forms.CharField(label="Ингридиенты", widget=forms.Textarea)
    description = forms.CharField(label="Описание", widget=forms.Textarea)
    cooking_steps = forms.CharField(label="Шаги приготовления", widget=forms.Textarea)
    cooking_time = forms.TimeField(label="Время приготовления",
                                   input_formats=['%H:%M'], widget=forms.TimeInput(format='%H:%M'))
    image = forms.ImageField()
    author = forms.CharField(label="Автор", max_length=100)

