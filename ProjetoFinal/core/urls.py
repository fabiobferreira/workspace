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
from . views import (
    home, 
    lista_pessoas,
    pessoas_novo,
    pessoas_update,
     
    lista_veiculos,
    veiculos_novo,
    veiculos_update,
    
    lista_rotativo,    
    rotativo_novo,
    rotativo_update,
    
    lista_mensalistas,
    mensalistas_novo,
    mensalistas_update,
    
    lista_movmensalistas,   
    movmensalistas_novo,
    movmensalistas_update
    )

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas_novo', pessoas_novo, name='core_pessoas_novo'),
    path('pessoas_update', pessoas_update, name='core_pessoas_update'),
        
    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('veiculos_novo', veiculos_novo, name='core_veiculos_novo'),
    path('veiculos_update', veiculos_update, name='core_veiculos_update'),
    
    path('rotativo', lista_rotativo, name='core_lista_rotativo'),
    path('rotativo_novo', rotativo_novo, name='core_rotativo_novo'),
    path('rotativo_update', rotativo_update, name='core_rotativo_update'),
    
    path('mensalistas', lista_mensalistas, name='core_lista_mensalistas'),
    path('mensalistas_novo', mensalistas_novo, name='core_mensalistas_novo'),
    path('mensalistas_update', mensalistas_update, name='core_mensalistas_update'),
    
    path('movmensalistas', lista_movmensalistas, name='core_lista_movmensalistas'),
    path('movmensalistas_novo', movmensalistas_novo, name='core_movmensalistas_novo'),
    path('movmensalistas_update', movmensalistas_update, name='core_movmensalistas_update'),
    
]
