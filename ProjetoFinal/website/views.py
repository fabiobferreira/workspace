from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'website/index.html')

def contato(request):
    contato = {}
    contato['nome'] = request.POST.get('nome')
    contato['email'] = request.POST.get('email') 
    contato['endereco'] = request.POST.get('endereco') 
    contato['cidade'] = request.POST.get('cidade') 
    contato['uf'] = request.POST.get('uf')
    contato['cep'] = request.POST.get('cep') 
    contato['mensagem'] = request.POST.get('mensagem')
    contato['receber_noticias'] = request.POST.get('receber_noticias')     
    return render(request, 'website/contato.html')

def servicos(request):
    return render(request, 'website/servicos.html')

def sobre(request):
    return render(request, 'website/sobre.html')

def planos(request):
    return render(request, 'website/planos.html')



