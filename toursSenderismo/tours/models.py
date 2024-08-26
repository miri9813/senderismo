from django.db import models
from django.contrib.auth.models import User


class Tour(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    latitud = models.TextField(null=True, blank=True)  # Latitud
    longitud = models.TextField(null=True, blank=True)  # Longitud
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")

    def __str__(self):
        return self.nombre
    
class Reseña(models.Model):
    tour = models.ForeignKey(Tour, related_name='reseñas', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return str + '{self.usuario.username} - {self.tour.nombre}'

from django.db import models
from django.contrib.auth.models import User

class Reserva(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad_personas = models.IntegerField(default=1)
    total_precio = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_realizacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.tour.nombre}"

