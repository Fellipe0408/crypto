from django.shortcuts import render, redirect
from .models import Registro

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            user = Registro.objects.get(email=email, senha=senha)
            # Aqui você pode usar sessions para simular login
            request.session['usuario_id'] = user.id
            return redirect('home')  # ou qualquer outra página
        except Registro.DoesNotExist:
            return render(request, 'registration/login.html', {'erro': 'Email ou senha inválidos.'})
    
    return render(request, 'registration/login.html')