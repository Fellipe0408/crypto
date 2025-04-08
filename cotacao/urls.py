from django.urls import path
from . import views

urlpatterns = [
    path('', views.cotacao, name='cotacao'),
]