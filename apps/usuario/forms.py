from django.contrib.auth.models import User
from django import forms
from django.forms import fields



class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']