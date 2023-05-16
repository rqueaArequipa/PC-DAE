from django.shortcuts import render
from rest_framework import viewsets, permissions
from examen.models import Categoria, Post
from .serializers import CategoriaSerializer, PostSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
