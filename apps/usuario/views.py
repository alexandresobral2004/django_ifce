from django.shortcuts import render,redirect
from .forms import UsuarioForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def add_user(request):
    template_name = 'usuario/add_user.html'
    context = {}
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            messages.success(request,"Usuário Salvo com Sucesso!")
    form = UsuarioForm()
    context['form'] = form
    return render(request,template_name,context)


class UserLogin(LoginView):
    template_name = 'usuario/user_login.html'
    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            print(password)
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Login Realizado com Sucesso!')
                return redirect('usuario:dashboard')
            messages.error(request,'Login ou senha inválidos!')
            return redirect('usuario:user_login')



@login_required(login_url='usuario:user_login')
def user_logout(request):
    logout(request)
    return redirect('usuario:user_login')

@login_required(login_url='usuario:user_login')
def dashboard(request):
    template_name = 'usuario/dashboard.html'
    return render(request,template_name,{})