
# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from sqlite3 import IntegrityError
import random
from .models import Reservacion
from .models import Reservacion
from .forms import ReservacionForm

def home(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReservacionForm(request.POST)
        if form.is_valid():
            reservacion = form.save(commit=False)
            reservacion.usuario = request.user
            reservacion.save()
            return redirect('reservaciones')
    else:
        form = ReservacionForm()
    return render(request, 'registration/home.html', {'form': form})

def habit_view(request):
    return render(request, 'registration/habitaciones.html')

@login_required
def reservar(request):
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():
            reservacion = form.save(commit=False)
            reservacion.usuario = request.user
            reservacion.save()
            return redirect('mis_reservaciones')
    else:
        form = ReservacionForm()
    return render(request, 'registration/reservar.html', {'form': form})

    
@login_required
def reservaciones(request):
    reservaciones = Reservacion.objects.filter(usuario=request.user)
    return render(request, 'registration/reservacion_list.html', {'reservaciones': reservaciones})

def signup_view(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registration/signup.html', {
                    'form': UserCreationForm(),
                    'error': 'User already exists'
                })
        else:
            return render(request, 'registration/signup.html', {
                'form': UserCreationForm(),
                'error': 'Passwords do not match'
            })


def contacto_view(request):
    urls = [
        'https://www.instagram.com/angel_x___/',
        'https://www.instagram.com/yordi24k/',
        'https://www.instagram.com/diegosalazaar3/',
        'https://www.instagram.com/jorge__alamillo/'
    ]
    selected_url = random.choice(urls)
    return redirect(selected_url)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

def signup_view(request):
    # lógica para el signup
    if request.method == 'GET':
        return render(request, 'registration/signup.html',{
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user =User.objects.create_user(username=request.POST['username'],password=request.POST['password1'] )
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html'), {
                    'form': UserCreationForm,
                    "error": 'User already exist'
                }
        return render(request,'signup.html'), {
            'form': UserCreationForm,
            "error": 'Password do not match'
        }
    
def logout_view(request):
    logout(request)
    return redirect('home')

