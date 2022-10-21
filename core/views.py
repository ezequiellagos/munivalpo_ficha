from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect


@login_required(login_url='/login/')
def home(request):
    return render(request, 'core/home.html')

def login(request):
    mensaje = ''

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            mensaje = 'Usuario o contraseña incorrectos'
    
    data = {
        'mensaje': mensaje
    }
    return render(request, 'core/login.html', data)

def logout(request):
    auth_logout(request)
    return redirect('core_login')