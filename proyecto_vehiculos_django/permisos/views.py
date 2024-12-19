from django.shortcuts import render , redirect
from django.contrib.auth.models import User, Group, Permission
from .forms import RegistroForm 

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            # Asignación el grupo comun al nuevo usuario
            grupo_usuarios, _ = Group.objects.get_or_create(name= 'editores')
            user.groups.add(grupo_usuarios)
            
            permisos = Permission.objects.filter(codename__in=['add_vehiculos', 'view_vehiculos'])
            grupo_usuarios.permissions.add(*permisos)
            
            permisos_usuario = Permission.objects.filter(codename__in=['add_vehiculos', 'view_vehiculos'])
            user.user_permissions.add(*permisos_usuario)
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'permisos/registrar_usuarios.html', {'form': form})