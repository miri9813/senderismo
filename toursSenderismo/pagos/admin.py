
from django.contrib import admin
from .models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'fecha')
    search_fields = ('nombre',)
    list_filter = ('fecha',)
