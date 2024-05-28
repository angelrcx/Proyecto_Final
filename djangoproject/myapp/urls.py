# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),  # Página de inicio
    path('reservar/', views.reservar, name='reservar'),
    path('reservaciones/', views.reservaciones, name='reservaciones'),
    path('login/', views.login_view, name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name = "logout"),
    path('contacto/',views.contacto_view,name = "contacto"),
    path('habitaciones/',views.habit_view,name="habitaciones"),

]
