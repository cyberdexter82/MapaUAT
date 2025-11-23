from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Ubicacion 

# --- 1. VISTA DE INICIO (PORTADA) ---
def inicio_view(request):
    return render(request, 'inicio2.html')

# --- 2. VISTA DE LOGIN ---
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == 'POST':
        matricula = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=matricula, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'Login.html', {'error': 'Matrícula o contraseña incorrecta'})

    return render(request, 'Login.html')

# --- 3. VISTA DE REGISTRO ---
def registro_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        matricula = request.POST.get('matricula')
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        confirmar = request.POST.get('confirmar')

        if password != confirmar:
            return render(request, 'registro.html', {'error': 'Las contraseñas no coinciden'})
        
        if User.objects.filter(username=matricula).exists():
            return render(request, 'registro.html', {'error': 'Esa matrícula ya está registrada'})

        try:
            user = User.objects.create_user(username=matricula, email=correo, password=password, first_name=nombre)
            user.save()
            login(request, user)
            return redirect('home')
        except:
            return render(request, 'registro.html', {'error': 'Error al crear usuario'})

    return render(request, 'registro.html')

# --- 4. VISTA DE PERFIL ---
@login_required(login_url='login')
def perfil_view(request):
    user = request.user
    mensaje = None
    error = None

    if request.method == 'POST':
        if 'update_info' in request.POST:
            user.first_name = request.POST.get('nombre')
            user.email = request.POST.get('correo')
            user.save()
            mensaje = "¡Datos actualizados correctamente!"

    return render(request, 'perfil.html', {'user': user, 'mensaje': mensaje, 'error': error})

# --- 5. RECUPERAR CONTRASEÑA ---
def recuperar_view(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        correo = request.POST.get('correo')
        nueva_pass = request.POST.get('password')
        confirmar = request.POST.get('confirmar')

        if nueva_pass != confirmar:
            return render(request, 'recuperar.html', {'error': 'Las contraseñas no coinciden'})

        try:
            user = User.objects.get(username=matricula, email=correo)
            user.set_password(nueva_pass)
            user.save()
            return redirect('login')
        except User.DoesNotExist:
            return render(request, 'recuperar.html', {'error': 'Datos incorrectos'})

    return render(request, 'recuperar.html')

# --- 6. CERRAR SESIÓN ---
def logout_view(request):
    logout(request)
    return redirect('home')

# --- 7. VISTA DE INSTRUCCIONES ---
def instrucciones_view(request):
    return render(request, 'instrucciones.html')

# --- 8. VISTA DEL MAPA COMPLETO (SISTEMA ADMIN) ---
# ¡OJO! He quitado el @login_required de aquí para que los invitados puedan entrar
def mapa_view(request):
    puntos = Ubicacion.objects.all().order_by('nombre')
    return render(request, 'Sitio_web.html', {'puntos': puntos})

# --- 9. INVITADO ---
def invitado_view(request):
    if request.method == 'POST':
        return redirect('instrucciones')
    return render(request, 'invitado.html')