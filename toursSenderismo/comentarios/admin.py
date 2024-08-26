
from django.contrib import admin
from .models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'contenido', 'fecha')
    search_fields = ('nombre', 'email', 'contenido')
    list_filter = ('fecha',)
