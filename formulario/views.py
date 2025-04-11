from django.shortcuts import render

def formulario(request):
    return render(
        request, 
        'form/formulario.html'
    )
