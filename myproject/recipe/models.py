from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.TimeField()
    image = models.ImageField(upload_to='dishes_img/')
    author = models.CharField(max_length=100)
    ingredients = models.TextField()
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.name
