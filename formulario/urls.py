from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('gravar/', views.formulario_gravar, name='formulario_gravar'),
]