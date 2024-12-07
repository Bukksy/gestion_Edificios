from django.urls import path
from . import views

app_name='visitas'

urlpatterns = [
    path('', views.visitas, name='visitas'),
    path('registrar', views.registrar, name='registrar'),
    path('historial/', views.historial_visitas, name='historial_visitas'),
]