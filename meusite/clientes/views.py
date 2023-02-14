
from django.shortcuts import render
from http.client import HTTPResponse

# Create your views here.

def clientes(request):
    return HTTPResponse('Maria, João, José')

def cliente_detalhe(request):
    return HTTPResponse('Cliente Detalhe')