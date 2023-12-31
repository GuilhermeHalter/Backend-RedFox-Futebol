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
from django.urls import include, path
from usuario.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter

from RedFox.views import CategoriaViewSet,EstadiosViewSet,IngressoViewSet,JogosViewSet,TimeViewSet
from uploader.views import  ImageUploadViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"estadios", EstadiosViewSet)
router.register(r"ingressos", IngressoViewSet)
router.register(r"jogos", JogosViewSet)
router.register(r"times", TimeViewSet)
router.register(r"imagem", ImageUploadViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)