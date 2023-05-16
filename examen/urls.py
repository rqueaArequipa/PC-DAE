#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index, name='index'),
    path('categoria/<int:categoria_id>/', views.Category, name='categoria')
]