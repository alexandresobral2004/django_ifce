from django.contrib import admin
from django.urls import include, path
from apps.core import views


app_name = 'aluno'

from . import views

urlpatterns = [

    #adicionando a view do core
    path('',views.HomeView.as_view(),name='home'),
    path('novo/',views.AddAluno,name='add_aluno'),
    path('lista/',views.lista_Alunos,name='lista_alunos'),
    path('editar/<int:id_aluno>/',views.edit_aluno,name='edit_aluno'),
    path('delete/<int:id_aluno>/',views.deleteAluno,name='delete_aluno'),
    path('usuario/', include('usuario.urls', namespace='usuario')),
   
   
  
]
