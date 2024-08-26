from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Tour
from .forms import TourForm
##Agregar el @login required a cualquier funcion que ocupe 

def nuevo_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tours/')
    else:
        form = TourForm()
    return render(request, 'tours/nuevo_tour.html', {'form': form})



def apartar_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tours/apartar_tour.html', {'tour': tour})


def confirmacion_pago(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tours/confirmacion_pago.html', {'tour': tour})


def proceso_pago(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        # Procesar el pago aquí
        return redirect('confirmacion_pago', tour_id=tour.id)
    return render(request, 'tours/proceso_pago.html', {'tour': tour})

from django.shortcuts import render, get_object_or_404
from .models import Tour, Reseña
from .forms import ReseñaForm

def detalles_tour(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    reseñas = Reseña.objects.filter(tour=tour)
    
    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            reseña = form.save(commit=False)
            reseña.tour = tour
            reseña.usuario = request.user
            reseña.save()
            return redirect('detalles_tour', tour_id=tour.id)
    else:
        form = ReseñaForm()

    return render(request, 'tours/detalles_tour.html', {
        'tour': tour,
        'reseñas': reseñas,
        'form': form
    })
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tour, Reserva

def proceso_pago(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        cantidad_personas = int(request.POST.get('cantidad_personas', 1))
        total_precio = tour.precio * cantidad_personas

        reserva = Reserva(
            tour=tour,
            usuario=request.user,
            cantidad_personas=cantidad_personas,
            total_precio=total_precio,
            pagado=True  # Asegúrate de que el pago esté marcado como realizado
        )
        reserva.save()

        return redirect('confirmacion_pago', tour_id=tour.id)
    return render(request, 'tours/proceso_pago.html', {'tour': tour})


def lista_reservas(request):
    reservas_realizadas = Reserva.objects.filter(usuario=request.user, fecha_realizacion__isnull=False)
    reservas_pendientes = Reserva.objects.filter(usuario=request.user, fecha_realizacion__isnull=True, pagado=True)

    return render(request, 'tours/lista_reservas.html', {
        'reservas_realizadas': reservas_realizadas,
        'reservas_pendientes': reservas_pendientes
    })
from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render, get_object_or_404
from .models import Tour, Reserva
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def lista_inscritos_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    reservas = Reserva.objects.filter(tour=tour)

    # Calcular el total de ganancias
    total_ganancias = sum(reserva.total_precio for reserva in reservas)

    return render(request, 'tours/lista_inscritos_tour.html', {
        'tour': tour,
        'reservas': reservas,
        'total_ganancias': total_ganancias
    })

def lista_tours(request):
    query = request.GET.get('q')
    if query:
        tours = Tour.objects.filter(nombre__icontains=query)
    else:
        tours = Tour.objects.all()

    return render(request, 'tours/lista_tours.html', {'tours': tours})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Reserva

@login_required
def mis_tours(request):
    # Obtener reservas del usuario
    reservas_realizadas = Reserva.objects.filter(usuario=request.user, fecha_realizacion__isnull=False)
    reservas_pendientes = Reserva.objects.filter(usuario=request.user, fecha_realizacion__isnull=True, pagado=True)
    
    return render(request, 'tours/mis_tours.html', {
        'reservas_realizadas': reservas_realizadas,
        'reservas_pendientes': reservas_pendientes
    })
