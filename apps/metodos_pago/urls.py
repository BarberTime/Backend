from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MetodoPagoViewSet

router = DefaultRouter()
router.register(r'metodos_pago', MetodoPagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
