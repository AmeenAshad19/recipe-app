from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from recipes.views import RecipeViewSet, RecipeListView

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/recipes/', RecipeListView.as_view(), name='recipe-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
