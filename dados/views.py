from django.shortcuts import render
from .models import Pessoa

# Create your views here.

def dados(request):
    contexto = {
        'title' : 'Dados'
    }
    return render (
        request,
        'dados/login.html',
        contexto
    )

def conclusao(request):
    #Salvar os dados da tela para o banco
    nova_pessoa = Pessoa()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.email = request.POST.get('email')
    nova_pessoa.save()
    
    return dados(request)