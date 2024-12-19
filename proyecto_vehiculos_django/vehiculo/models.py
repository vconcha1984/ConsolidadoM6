from django.db import models

# Create your models here.

marcas = (
    ('Ford', 'Ford'),
    ('Fiat', 'Fiat'),
    ('Chevrolet', 'Chevrolet'),
    ('Toyota', 'Toyota')
)
categorias = (
    ('Particular', 'Particular'),
    ('Transporte', 'Transporte'),
    ('Carga', 'Carga')
)
class Vehiculos(models.Model):
    marca = models.CharField(max_length=20,choices=marcas, default='ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=categorias ,default='particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        permissions = [
            ("add_vehiculo", "Puede agregar vehículos"),
            ("view_vehiculo", "Puede ver vehículos"),
            ("delete_vehiculo", "Puede eliminar vehículos"),
            ("update_vehiculo", "Puede actualizar vehículos"),
        ]