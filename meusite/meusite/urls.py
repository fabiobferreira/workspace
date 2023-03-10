"""meusite URL Configuration

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
from django.contrib import admin
from django.urls import path
from .views import home
from clientes.views import clientes, cliente_detalhe
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', home),
    path('clientes/', clientes),
    path('cliente/', cliente_detalhe),
    path('admin/', admin.site.urls),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Use include() to add paths from the catalog application
from django.urls import include

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='127.0.0.1:8000/catalog/', permanent=True)),
]