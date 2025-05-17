"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('/', admin.site.urls),
    path('api/v1/', include('apps.usuario.urls')), 
    path('api/v1/', include('apps.servicio.urls')),
    path('api/v1/', include('apps.resenia.urls')),
    path('api/v1/', include('apps.negocio.urls')),
    path('api/v1/', include('apps.horario.urls')),
    path('api/v1/', include('apps.cita.urls')),
    path('api/v1/', include('apps.categoria.urls')),
    path('api/v1/', include('apps.rol.urls')),
    path('api/v1/', include('apps.metodos_pago.urls')),
    path('api/v1/', include('apps.empleados.urls')),
    path('api/v1/', include('apps.imagenes_negocio.urls')),
    path('api/v1/', include('apps.pago.urls')),
    path('api/v1/', include('apps.ciudad.urls')),
    path('api/v1/', include('apps.cliente.urls')),
    path('api/v1/', include('apps.authLogin.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # Configuración para producción
    urlpatterns += [
        path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
        path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
    ]
