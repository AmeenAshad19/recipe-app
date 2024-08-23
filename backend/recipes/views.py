from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import filters
from django.db.models import Q
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework import viewsets


class RecipeListView(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        search_term = self.request.query_params.get('search', None)
        if search_term:
            queryset = queryset.filter(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term) |
                Q(search_tags__icontains=search_term)
            )
        return queryset

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description', 'search_tags')

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', None)
        if search_term:
            # Search in title and description
            queryset = queryset.filter(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term) |
                Q(search_tags__icontains=search_term)
            )
        return queryset
