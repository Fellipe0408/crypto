from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

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

@login_required
@require_POST
def adicionar_comentario(request):
    try:
        data = json.loads(request.body)
        texto = data.get('texto', '').strip()
        if not texto:
            return JsonResponse({'error': 'Comentário vazio não permitido.'}, status=400)

        # Use o nome correto do modelo
        comentario = Comentario.objects.create(usuario=request.user, texto=texto)

        return JsonResponse({
            'success': True,
            'message': 'Comentário adicionado com sucesso',
            'usuario': request.user.username,
            'texto': comentario.texto,
            'data_postagem': comentario.data_postagem.strftime('%d/%m/%Y %H:%M'),
            'foto_perfil_url': request.user.profile.photo.url if hasattr(request.user, 'profile') else 'URL_PADRAO',  # Adicione a URL da foto de perfil
        })
    except Exception as e:
        return JsonResponse({'error': 'Erro ao processar comentário: ' + str(e)}, status=500)


@require_POST
def remover_comentario(request, id):
    try:
        comentario = Comentario.objects.get(id=id)
        comentario.delete()
        return JsonResponse({
            'success': True,
            'message': "Comentário deletado com sucesso",
        })
    except Comentario.DoesNotExist:
        return JsonResponse({'error': 'Comentário não encontrado.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': 'Erro ao deletar comentário: ' + str(e)}, status=500)