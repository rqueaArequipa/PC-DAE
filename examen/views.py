from django.shortcuts import render
from .models import Categoria, Post

def Index(request):
    list_post = Post.objects.all()
    list_cat = Categoria.objects.all()
    context = {
        'posts' : list_post,
        'cats' : list_cat
    }
    return render(request, 'index.html', context)

def Category(request, categoria_id):
    list_post = Post.objects.filter(categoria=categoria_id)
    list_cat = Categoria.objects.all()
    context = {
        'posts' : list_post,
        'cats' : list_cat
    }
    return render(request, 'category.html', context)
