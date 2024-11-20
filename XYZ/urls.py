from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('visitas/', include('visitas.urls')),
    path('reservas/', include('reservas.urls')),
]
