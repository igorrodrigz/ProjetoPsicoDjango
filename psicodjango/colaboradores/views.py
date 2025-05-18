from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ColaboradorForm
from .forms_questionario import QuestionarioForm
from .models import QuestionarioResposta

@login_required
def index_colaborador(request):
    return render(request, 'colaboradores/index.html')

def criar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('colaborador_sucesso')
    else:
        form = ColaboradorForm()
    return render(request, 'colaboradores/criar_colaborador.html', {'form': form})

def colaborador_sucesso(request):
    return render(request, 'colaboradores/colaborador_sucesso.html')

@login_required
def questionario_colaborador(request):
    if request.method == 'POST':
        form = QuestionarioForm(request.POST)
        if form.is_valid():
            respostas = form.cleaned_data
            QuestionarioResposta.objects.create(
                colaborador=request.user,
                **respostas
            )
            return render(request, 'colaboradores/questionario_sucesso.html')
    else:
        form = QuestionarioForm()
    return render(request, 'colaboradores/questionario.html', {'form': form})
