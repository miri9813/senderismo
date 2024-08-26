# comentarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_comentarios, name='lista_comentarios'),  # URL para listar comentarios
    path('nuevo/', views.nuevo_comentario, name='nuevo_comentario'),  # URL para crear un nuevo comentario
]
