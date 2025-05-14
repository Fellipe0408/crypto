from django.shortcuts import render

def profile_view(request):
       # Your logic here
    return render(request, 'users/profile.html')

