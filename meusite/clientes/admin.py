from django.contrib import admin

# Register your models here.

from .models import Cliente, Telefone, CPF, Departamento

#class ClienteAdmin(admin.ModelAdmin):
    #fields = ('nome', 'endereco')
    #list_display = ('id', 'nome', 'endereco', 'email')
    #list_filter = ('departamentos')
    #search_fields = ('id', 'nome', 'email', 'departamentos__nome' )

#admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Cliente)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)

