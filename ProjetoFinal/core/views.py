from django.shortcuts import redirect, render
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo,
    Mensalista,
    MovMensalista,
    )


from .form import PessoaForm

# Create your views here.

def home(request):
    context = {'mensagem': 'Olá, Mundo'}
    return render(request, 'core/index.html', context)

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html',data)

def pessoas_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})

def lista_rotativo(request):
    rotativo = MovRotativo.objects.all()
    return render(request, 'core/lista_rotativo.html', {'rotativo': rotativo})

def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas})

def lista_movmensalistas(request):
    movmensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_movmensalistas.html', {'movmensalistas': movmensalistas})