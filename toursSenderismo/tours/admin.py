# tours/admin.py

from django.contrib import admin
from .models import Tour

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'duracion', 'precio')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('duracion',)
