from django.shortcuts import redirect, render
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo,
    Mensalista,
    MovMensalista,
    )


from .form import MovRotativoForm, PessoaForm, VeiculoForm

# Create your views here.

def home(request):
    context = {'mensagem': 'Página Inicial'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)

def pessoas_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm(request.POST or None)
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)

def veiculos_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def lista_rotativo(request):
    rotativo = MovRotativo.objects.all()
    form = MovRotativo(request.POST or None)
    data = {'rotativo': rotativo, 'form': form}
    return render(request, 'core/lista_rotativo.html', )

def rotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_rotativo')


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas})

def lista_movmensalistas(request):
    movmensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_movmensalistas.html', {'movmensalistas': movmensalistas})