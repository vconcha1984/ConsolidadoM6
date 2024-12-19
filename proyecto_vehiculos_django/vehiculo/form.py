from django import forms
from .models import Vehiculos

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

class VehiculoForm(forms.ModelForm):
    marca  = forms.ChoiceField(choices=marcas)
    modelo = forms.CharField(max_length=100)
    serial_carroceria = forms.CharField(max_length=50)
    serial_motor = forms.CharField(max_length=50)
    categoria = forms.ChoiceField(choices=categorias)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        model = Vehiculos
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']