from django.shortcuts import render, get_object_or_404
from .models import Bodega, Vino, Reseña
from .forms import BodegaForm, VinoForm, ReseñaForm


# Create your views here.

def inicio(request):
    return render(request, 'vinos/inicio.html')

def crear_bodega(request):
    if request.method == 'POST':
        form = BodegaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'vinos/exito.html')
    else:
        form = BodegaForm()
    return render(request, 'vinos/formulario.html', {'form': form, 'titulo': 'Nueva Bodega'})

def buscar_vino(request):
    query = request.GET.get('q')
    resultados = Vino.objects.filter(nombre__icontains=query) if query else None
    return render(request, 'vinos/buscar.html', {'resultados': resultados})
