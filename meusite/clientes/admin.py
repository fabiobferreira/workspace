from django.contrib import admin

# Register your models here.

from .models import Cliente, Telefone

admin.site.register(Cliente)
admin.site.register(Telefone)
