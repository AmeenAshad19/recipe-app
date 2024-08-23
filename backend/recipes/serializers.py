
from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'ingredients', 'instructions', 'search_tags', 'is_vegetarian', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None
