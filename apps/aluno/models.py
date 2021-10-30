from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100,help_text='Nome do Aluno')
    cpf = models.CharField(max_length=12,help_text='CPF do Aluno',blank=False,default='')
    email = models.CharField(max_length=100,help_text='e-mail',default='')
    data_nasc = models.DateField('Data de Nascimento',auto_now=False,auto_now_add=False,blank=True,default='')



class Meta:
    ordering=['-id']

#exibe o nome do aluno no admin no lugar no nome do objeto
def __str__(self):
    return self.nome