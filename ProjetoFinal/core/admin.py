from django.contrib import admin
from .models import Pessoa, Marca, Veiculo

# Register your models here.

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
