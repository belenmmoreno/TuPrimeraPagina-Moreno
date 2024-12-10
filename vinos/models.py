from django.db import models

# Create your models here.

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre
    
class Vino(models.Model):
    nombre = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=[('Tinto', 'Tinto'), ('Blanco', 'Blanco'), ('Rosado', 'Rosado')])
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    def __str__(self):
        return self.nombre
    
class Reseña(models.Model):
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    calificacion = models.IntegerField()
    def __str__(self):
        return f'Reseña de {self.usuario} sobre {self.vino}'

