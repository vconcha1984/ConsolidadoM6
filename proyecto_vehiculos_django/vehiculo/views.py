from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from .form import VehiculoForm
from .models import Vehiculos

# Create your views here.
@login_required()
@permission_required('vehiculo.view_vehiculos', raise_exception=True)
def index(request):
    vehiculo = Vehiculos.objects.all()
    condicion = []
    for vcl in vehiculo:
        if vcl.precio < 10000:
            condicion.append('bajo')
        elif vcl.precio >= 10000 and vcl.precio < 30000:
            condicion.append('medio')
        elif vcl.precio >= 30000:
            condicion.append('alto')
        else:
            condicion.append('error')
    vehiculos_final = zip(vehiculo, condicion)
    return render(request, 'vehiculos/index.html',{'vehiculos':vehiculos_final})

@login_required()
@permission_required('vehiculo.view_vehiculos', raise_exception=True)
@permission_required('vehiculo.add_vehiculos', raise_exception=True)
def add(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo:index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/add_vehiculo.html', {'form':form})
