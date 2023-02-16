"""estacionamento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos,
    lista_rotativo,
    lista_mensalistas,
    lista_movmensalistas,
    pessoas_novo,
    veiculos_novo
    )


urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas_novo', pessoas_novo, name='core_pessoas_novo'),
    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('veiculos_novo', veiculos_novo, name='core_veiculos_novo'),
    path('rotativo', lista_rotativo, name='core_lista_rotativo'),
    path('mensalistas', lista_mensalistas, name='core_lista_mensalistas'),
    path('movmensalistas', lista_movmensalistas, name='core_lista_movmensalistas'),
]
