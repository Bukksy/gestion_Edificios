from django.shortcuts import render, redirect
from .models import Visita
from django.utils.timezone import now, timedelta
from django.contrib import messages 
from usuarios.models import Usuario


def visitas(request):
    return render(request, 'visitas/visitas.html')

def agregar_visita(request):
    if request.method == 'POST':
        residente_id = request.POST.get('residente')
        visitante_nombre = request.POST.get('visitante_nombre')

        try:
            residente = Usuario.objects.get(id=residente_id, rol='residente')
        except Usuario.DoesNotExist:
            return render(request, 'agregar_visita.html', {'error': 'Residente no encontrado o no válido'})

        fecha_entrada = now()

        visita = Visita.objects.create(
            residente=residente,
            visitante_nombre=visitante_nombre,
            fecha_entrada=fecha_entrada,
            fecha_salida=request.POST.get('fecha_salida')
        )

        # Agregar mensaje de éxito
        messages.success(request, 'Visita registrada exitosamente.')

        return redirect('visitas')  # Redirige a la lista de visitas (u otra página donde quieres mostrar el mensaje)
    else:
        residentes = Usuario.objects.filter(rol='residente')
        hora_actual = now().strftime('%Y-%m-%d %H:%M:%S')  # Obtener la hora actual en formato string
        return render(request, 'visitas/agregar_visita.html', {'residentes': residentes, 'hora_actual': hora_actual})