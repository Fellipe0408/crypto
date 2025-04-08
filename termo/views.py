from django.shortcuts import render

def termo(request):
    return render(
        request, 
        'termo/termos&condicoes.html'
    )