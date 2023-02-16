from django.shortcuts import render
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo,
    Mensalista,
    MovMensalista,
    )


# Create your views here.

def home(request):
    context = {'mensagem': 'Olá, Mundo'}
    return render(request, 'core/index.html', context)

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})

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