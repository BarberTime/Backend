from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImagenNegocioViewSet

router = DefaultRouter()
router.register(r'imagenes_negocio', ImagenNegocioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
