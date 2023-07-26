from django.shortcuts import render, redirect
from django.contrib.auth.models import User


usuarios = [
    {
        'nombre' : "Gabriel",
        'apellido' : "Muñoz",
        'direccion' : "Avenida 123",
        'correo' : "gabriel_2023@example.com",
    },
    {
        'nombre' : "Jimena",
        'apellido' : "Lopez",
        'direccion' : "Calle 28",
        'correo' : "jimena.lopez@example.com",
    },
    {
        'nombre' : "Laura",
        'apellido' : "Ramirez",
        'direccion' : "pasaje b-31",
        'correo' : "laura.ramirez@example.com",
    },
    {
        'nombre' : "Carlos",
        'apellido' : "Sanchez",
        'direccion' : "Calle 12",
        'correo' : "carlos.sanchez@example.com",
    },
    {
        'nombre' : "Pedro",
        'apellido' : "Gonzalez",
        'direccion' : "Carrera 45",
        'correo' : "pedro.gonzalez@example.com",
    },
]
# Create your views here.

def index(request):
    return render(request, 'app_landing_page/index.html')

def lista_usuarios(request):
    auxiliar = {
        'usuarios': usuarios
    }
    return render(request, 'app_landing_page/usuarios.html', auxiliar)

def registrarse(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        repita_contraseña = request.POST.get('repita_contraseña')
        nombre_usuario = correo.split('@')[0]
        nuevo_usuario, creado = User.objects.get_or_create(username=nombre_usuario, email=correo)
        if not creado:
            return render(request, 'app_landing_page/registrarse.html')
        nuevo_usuario.set_password(contraseña)
        nuevo_usuario.first_name = nombre
        nuevo_usuario.last_name = apellido
        nuevo_usuario.save()
        
        
        return redirect('index')
    return render(request, 'app_landing_page/registrarse.html')

