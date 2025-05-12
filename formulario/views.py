from django.shortcuts import render
from .models import Registro
from django.shortcuts import redirect


def formulario(request):
    return render(request, 'form/formulario.html')

def formulario_gravar(request):
    if request.method == 'POST':
        form = Registro()
        form.nome = request.POST.get('name')
        form.email = request.POST.get('email')
        form.senha = request.POST.get('password')
        form.save()
        
        return render(request, 'form/formulario.html')
