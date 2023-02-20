import csv

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

@login_required
def home(request):
    context = {'mensagem': 'Ola mundo...'}
    return render(request, 'core/index.html', context)


@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)

@login_required
def pessoas_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')

@login_required
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

@login_required
def pessoas_delete(request, id):
    pessoas = Pessoa.objects.get(id=id)    
    if request.method == 'POST':
        pessoas.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoas})


@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm(request.POST or None)
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)

@login_required
def veiculos_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')

@login_required
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

@login_required
def veiculos_delete(request, id):
    veiculos = Veiculo.objects.get(id=id)    
    if request.method == 'POST':
        veiculos.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculos})


@login_required
def lista_rotativo(request):
    rotativo = MovRotativo.objects.all()
    form = MovRotativo(request.POST or None)
    data = {'rotativo': rotativo, 'form': form}
    return render(request, 'core/lista_rotativo.html', data)

@login_required
def rotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_rotativo')

@login_required
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

@login_required
def rotativo_delete(request, id):
    rotativo = MovRotativo.objects.get(id=id)    
    if request.method == 'POST':
        rotativo.delete()
        return redirect('core_lista_rotativo')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': rotativo})


@login_required
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm(request.POST or None)
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)

@login_required
def mensalistas_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')

@login_required
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

@login_required
def mensalistas_delete(request, id):
    mensalistas = Mensalista.objects.get(id=id)    
    if request.method == 'POST':
        mensalistas.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mensalistas})
    

@login_required
def lista_movmensalistas(request):
    movmensalistas = Mensalista.objects.all()
    form = MovMensalistaForm(request.POST or None)
    data = {'movmensalistas': movmensalistas, 'form': form}
    return render(request, 'core/lista_movmensalistas.html', data)

@login_required
def movmensalistas_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')

@login_required
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

@login_required
def movmensalistas_delete(request, id):
    movmensalistas = MovMensalista.objects.get(id=id)    
    if request.method == 'POST':
        movmensalistas.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': movmensalistas})
    
    
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View
class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)
class Pdf(View):

    def get(self, request):
        veiculos = Veiculo.objects.all()
        params = {
            'veiculos': veiculos,
            'request': request,
        }
        return Render.render('core/relatorio.html', params, 'relatorio_veiculos')
class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        veiculos = Veiculo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Marca', 'placa', 'Proprietario', 'Cor'])

        for veiculo in veiculos:
            writer.writerow(
                [veiculo.id, veiculo.marca, veiculo.placa, veiculo.proprietario,
                 veiculo.cor
                 ])
        return response
    