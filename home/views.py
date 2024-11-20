from django.shortcuts import render

def inicio(request):
    return render(request, '../templates/index.html')

def visitas(request):
    return render(request, 'visitas/visitas.html')

def reservas(request):
    return render(request, 'reservas/reservas.html')