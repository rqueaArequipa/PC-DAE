from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, PostViewSet
from django.urls import path, include

router = DefaultRouter()

router.register('categoria', CategoriaViewSet, 'categoria')
router.register('post', PostViewSet, 'post')

urlpatterns = [
    path('',include(router.urls)),
]