from django.db import models

class Pago(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Tour(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.DecimalField(max_digits=5, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
class Reserva(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    cantidad_personas = models.IntegerField()
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str+'Reserva para {self.tour.nombre} por {self.nombre}'