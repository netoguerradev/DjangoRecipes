from django.db import models

class Recipe(models.Model):
    title: models.CharField(max_length=65)
    description: models.CharField(max_length=165)
    slug: models.models.SlugField()
    preparation_time: models.integerField()
    preparation_time_unit: models.CharField( max_length=50)
    servings = models.integerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_Published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/cover/%Y/%m/%d/')