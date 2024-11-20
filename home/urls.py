from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('visitas/', views.visitas, name="visitas"),
    path('reservas/', views.reservas, name="reservas"),
]