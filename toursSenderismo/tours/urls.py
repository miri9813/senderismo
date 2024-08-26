# tours/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tours, name='lista_tours'),
    path('nuevo/', views.nuevo_tour, name='nuevo_tour'),
    path('<int:tour_id>/', views.detalles_tour, name='detalles_tour'),
    path('<int:tour_id>/proceso_pago/', views.proceso_pago, name='proceso_pago'),
    path('<int:tour_id>/apartar/', views.apartar_tour, name='apartar_tour'),
    path('confirmacion_pago/<int:tour_id>/', views.confirmacion_pago, name='confirmacion_pago'),
    path('<int:tour_id>/inscritos/', views.lista_inscritos_tour, name='lista_inscritos_tour'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('mis_tours/', views.mis_tours, name='mis_tours'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)