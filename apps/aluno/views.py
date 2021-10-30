from django.shortcuts import render,redirect, get_list_or_404,get_object_or_404
from aluno.models  import Aluno
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from aluno.forms import AlunoForm
from django.views.generic import TemplateView,CreateView,ListView



# def novoAluno(request):
#    template_name = 'aluno/add_aluno.html'
#    context = {}
#    form = AlunoForm()
#    context['form'] = form
#    return render(request,template_name,context)

class HomeView(TemplateView):
   template_name = 'aluno/lista_alunos.html'
   

# class AddAlunoView(CreateView):
#       template_name = 'aluno/add_aluno.html'
#       model = Aluno
#       form_class = AlunoForm
#       messages.success( "Usuário salvo com sucesso!")
#       success_url = 'aluno/add_aluno.html' 
    



# @login_required(login_url='usuario:user_login')
# class ListAlunosView(ListView):
#    model =Aluno
#    template_name = 'aluno/lista_alunos.html'
#    context_object_name = 'alunos'
#    paginate_by = 6

#    def get_queryset(self):
#        return Aluno.objects.all().order_by('-id')
@login_required(login_url='usuario:user_login')
def lista_Alunos(request):
    context = {}
    template_name = 'aluno/lista_alunos.html'
    alunos = Aluno.objects.all().order_by('-id')
    context = {'alunos':alunos} 
    return render(request,template_name,context)


@login_required(login_url='usuario:user_login')
def deleteAluno(request, id_aluno):
    aluno = Aluno.objects.get(id=id_aluno)
    aluno.delete()
    return redirect('aluno:lista_alunos')

@login_required(login_url='usuario:user_login')
def edit_aluno(request, id_aluno):
    template_name = 'aluno/add_aluno.html'
    context = {}
    aluno = get_object_or_404(Aluno, pk=id_aluno)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('aluno:lista_alunos')
    form = AlunoForm(instance=aluno)
    context['form'] = form
    return render(request, template_name, context)

# Create your views here.


# def home(request):
#     return render(request,'base.html',{})


@login_required(login_url='usuario:user_login')
def AddAluno(request):
    template_name = 'aluno/add_aluno.html'
    context = {}
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            # f = form.save(commit=False)
            form.save()
            messages.success(request, "Usuário salvo com sucesso!")
        else:
            messages.error(request, "Erro ao salvar dados!")
    form = AlunoForm()
    context['form'] = form
    return render(request,template_name,context)



  


# def lista_Alunos(request):
#     template_name = 'aluno/lista_alunos.html'
#     alunos = Aluno.objects.all().reverse()
#     context = { 'alunos':alunos  }
#     print(context)
#     return render(request,template_name,context)
