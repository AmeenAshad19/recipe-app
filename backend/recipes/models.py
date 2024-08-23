
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.JSONField()
    instructions = models.JSONField()
    search_tags = models.JSONField()
    is_vegetarian = models.BooleanField(default=False)
    # image_name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)


    def __str__(self):
        return self.title