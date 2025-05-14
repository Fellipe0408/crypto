from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home_view(request):
    comentarios = Comentario.objects.all().order_by('-data_postagem')
    if request.method == 'POST' and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.save()
            return redirect('home')
    else:
        form = ComentarioForm()

    return render(request, 'home/index.html', {'comentarios': comentarios, 'form': form})


@csrf_exempt  # Use isso apenas para testes, idealmente você deve usar o CSRF token
def adicionar_comentario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        texto = data.get('texto', '')
        if texto:
            comentario = Comentario(usuario=request.user, texto=texto)
            comentario.save()  # Salva o comentário na tabela home_comentario
            return JsonResponse({'status': 'success'}, status=201)
        return JsonResponse({'status': 'error', 'message': 'Texto vazio'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)
            