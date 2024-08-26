# pagos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pagos, name='lista_pagos'),  # URL para listar pagos
    path('nuevo/', views.nuevo_pago, name='nuevo_pago'),  # URL para crear un nuevo pago
   
]
