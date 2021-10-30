from django.apps import AppConfig


class AlunoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aluno'
    #muda o nome do app no admin
    verbose_name = 'Lista de Alunos' 

