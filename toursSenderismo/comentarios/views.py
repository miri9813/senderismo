from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Comentario
from .forms import ComentarioForm

def lista_comentarios(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save()  # Guarda el comentario en la base de datos
            return HttpResponseRedirect('/comentarios/')
    else:
        form = ComentarioForm()
    comentarios = Comentario.objects.all()
    return render(request, 'comentarios/lista_comentarios.html', {'form': form, 'comentarios': comentarios})

def nuevo_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/comentarios/')
    else:
        form = ComentarioForm()
    return render(request, 'comentarios/nuevo_comentario.html', {'form': form})
