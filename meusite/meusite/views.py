from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    sexo = 'm'
    nome = 'Pedro'
    lista = [
        {'nome': 'Pedro', 'sexo': 'm'},
        {'nome': 'Maria', 'sexo': 'f'},
        {'nome': 'Joaquina', 'sexo': 'f'},
        {'nome': 'João', 'sexo': 'm'},
    ]
    dados = {'lista': lista, 'sexo': sexo, 'nome': nome}
    return render(request, 'index.html', dados)