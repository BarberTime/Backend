from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReseniaViewSet

router = DefaultRouter()
router.register(r'resenias', ReseniaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
