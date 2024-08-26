from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Pago
from .forms import PagoForm

def lista_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'pagos/lista_pagos.html', {'pagos': pagos})

def nuevo_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pagos/')  # Redirige a la lista de pagos después de guardar el nuevo pago
    else:
        form = PagoForm()
    
    return render(request, 'pagos/nuevo_pago.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Tour, Reserva
from .forms import PagoForm

def procesar_pago(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    reserva = Reserva.objects.filter(tour=tour).last()  # Obtén la última reserva realizada para este tour
    
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            # Procesar el pago aquí (guardar en la base de datos, enviar confirmaciones, etc.)
            pago = form.save(commit=False)
            pago.reserva = reserva
            pago.save()
            
            messages.success(request, '¡Pago realizado exitosamente!')
            return redirect('detalle_tour', tour_id=tour.id)  # Ajusta la URL según tu configuración
    
    else:
        form = PagoForm()
    
    return render(request, 'pagos/procesar_pago.html', {'tour': tour, 'form': form})
