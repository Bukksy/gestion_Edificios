from django.urls import path
from . import views

app_name='visitas'

urlpatterns = [
    path('', views.visitas, name='visitas'),
]