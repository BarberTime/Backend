from django.urls import path
from .views import AuthLoginView    

urlpatterns = [
    path('auth/login/', AuthLoginView.as_view(), name='auth_login'),
]   