from django.shortcuts import render

def visitas(request):
    return render(request, 'visitas/visitas.html')
