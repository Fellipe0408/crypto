from django.shortcuts import render

def sobre(request):
    return render(
        request, 
        'sobre/sobre.html'
    )