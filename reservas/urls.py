from django.urls import path
from . import views

app_name='reservas'

urlpatterns = [
    path('', views.reservas, name='reservas'),
]