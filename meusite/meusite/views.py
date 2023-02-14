from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')

def clientes(request):
    return HttpResponse('Maria, João, José')

def cliente_detalhe(request):
    return HttpResponse('Cliente Detalhe')