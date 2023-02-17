from django.shortcuts import redirect, render
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo,
    Mensalista,
    MovMensalista,
    )

from .form import (
    PessoaForm, 
    VeiculoForm, 
    MovRotativoForm, 
    MensalistaForm, 
    MovMensalistaForm
    )

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

def pessoas_update(request, id):
    data = {}
    pessoas = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoas)
    data['pessoas'] = pessoas
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
        else:
            return render(request, 'core/pessoas_update.html', data)


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

def veiculos_update(request, id):
    data = {}
    veiculos = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculos)
    data['veiculos'] = veiculos
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
        else:
            return render(request, 'core/veiculos_update.html', data)


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

def rotativo_update(request, id):
    data = {}
    rotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=rotativo)
    data['rotativo'] = rotativo
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_rotativo')
        else:
            return render(request, 'core/rotativo_update.html', data)


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm(request.POST or None)
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)

def mensalistas_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')

def mensalistas_update(request, id):
    data = {}
    mensalistas = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalistas)
    data['mensalistas'] = mensalistas
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
        else:
            return render(request, 'core/mensalistas_update.html', data)


def lista_movmensalistas(request):
    movmensalistas = Mensalista.objects.all()
    form = MovMensalistaForm(request.POST or None)
    data = {'movmensalistas': movmensalistas, 'form': form}
    return render(request, 'core/lista_movmensalistas.html', data)

def movmensalistas_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')

def movmensalistas_update(request, id):
    data = {}
    movmensalistas = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movmensalistas)
    data['movmensalistas'] = movmensalistas
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
        else:
            return render(request, 'core/rotativo_movmensalistas.html', data)


    