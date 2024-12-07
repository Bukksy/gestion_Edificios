import re
from django.shortcuts import render
from .models import Visita
from django.utils import timezone
from django.contrib import messages 
from usuarios.models import Usuario
from django.core.exceptions import ValidationError


def validar_rut(rut):
    patron = r'^\d{7,8}-[0-9Kk]$'
    if not re.match(patron, rut):
        raise ValidationError('El RUT no tiene un formato válido. Debe ser xxxxxxxx-x')
    return rut


def visitas(request):
    return render(request, 'visitas/visitas.html')


def registrar(request):
    if request.method == 'POST':
        residente_id = request.POST.get('residente')
        rut_visitante = request.POST.get('rut_visitante')
        visitante_nombre = request.POST.get('visitante_nombre')
        fecha_salida = request.POST.get('fecha_salida')

        # Validar el formato del RUT
        try:
            validar_rut(rut_visitante)
        except ValidationError as e:
            messages.error(request, str(e))  # Mensaje de error para el RUT inválido
            return render(request, 'visitas/agregar_visita.html', {
                'residentes': Usuario.objects.filter(rol='residente'),
                'hora_actual': timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
            })  # Volver a renderizar la página con el mensaje de error

        # Validar si el RUT ya existe en las visitas registradas
        if Visita.objects.filter(rut_visitante=rut_visitante).exists():
            messages.error(request, 'Ya existe una visita registrada con ese RUT.')
            return render(request, 'visitas/agregar_visita.html', {
                'residentes': Usuario.objects.filter(rol='residente'),
                'hora_actual': timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
            })

        # Validar si el residente existe
        try:
            residente = Usuario.objects.get(id=residente_id, rol='residente')
        except Usuario.DoesNotExist:
            messages.error(request, 'Residente no encontrado o no válido.')
            return render(request, 'visitas/agregar_visita.html', {
                'residentes': Usuario.objects.filter(rol='residente'),
                'hora_actual': timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
            })

        # Validar fecha de salida
        if not fecha_salida:
            messages.error(request, 'La fecha de salida es obligatoria.')
            return render(request, 'visitas/agregar_visita.html', {
                'residentes': Usuario.objects.filter(rol='residente'),
                'hora_actual': timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
            })

        # Limitar el número de visitas a 5
        visitas_count = Visita.objects.filter(residente=residente).count()
        if visitas_count >= 5:
            messages.error(request, 'Este residente ya tiene el máximo de 5 visitas registradas.')
            return render(request, 'visitas/agregar_visita.html', {
                'residentes': Usuario.objects.filter(rol='residente'),
                'hora_actual': timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
            })

        # Validar si la visita ya fue registrada
        if Visita.objects.filter(residente=residente, visitante_nombre=visitante_nombre).exists():
            messages.error(request, 'Esta visita ya ha sido registrada.')
            return render(request, 'visitas/agregar_visita.html', {
                'residentes': Usuario.objects.filter(rol='residente'),
                'hora_actual': timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
            })

        # Registrar la visita
        fecha_entrada = timezone.localtime(timezone.now())

        Visita.objects.create(
            residente=residente,
            rut_visitante=rut_visitante,
            visitante_nombre=visitante_nombre,
            fecha_entrada=fecha_entrada,
            fecha_salida=fecha_salida
        )

        messages.success(request, 'Visita registrada exitosamente.')
        return render(request, 'visitas/agregar_visita.html', {
            'residentes': Usuario.objects.filter(rol='residente'),
            'hora_actual': timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
        })

    else:
        return render(request, 'visitas/agregar_visita.html', {
            'residentes': Usuario.objects.filter(rol='residente'),
            'hora_actual': timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
        })


def historial_visitas(request):
    visitas = Visita.objects.all().order_by('-fecha_entrada')
    return render(request, 'visitas/historial_visitas.html', {'visitas': visitas})
