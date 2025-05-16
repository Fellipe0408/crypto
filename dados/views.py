# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm

def login_view(request):
    erro = ''
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Loga o usuário
                return redirect('home')  # Redireciona após login
            else:
                erro = 'Usuário ou senha inválidos.'
    else:
        form = CustomLoginForm()
    
    return render(request, 'login.html', {'form': form, 'erro': erro})
