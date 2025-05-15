from django.urls import path
from .views import home_view
from .views import adicionar_comentario, remover_comentario

urlpatterns = [
    path('', home_view, name='home'),
    path('remover-comentario/<int:id>/', remover_comentario, name='remover_comentario'),
    path('adicionar_comentario/', adicionar_comentario, name='adicionar_comentario'),
]

