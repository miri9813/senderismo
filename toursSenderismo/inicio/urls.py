# inicio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # URL principal de la aplicación 'inicio'
]
