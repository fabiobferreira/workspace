from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nome

class CPF(models.Model):
    numero = models.CharField(max_length=15)
    data_exp = models.DateTimeField(auto_now=False)
       
# Create your models here.   
class Cliente(models.Model):
    nome = models.CharField(max_length=70, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    CPF = models.OneToOneField(CPF, null=True, blank=True, on_delete=models.CASCADE)
    departamentos = models.ManyToManyField(Departamento, null=True, blank=True)    
    
    def __str__(self):
        """String for representing the Model object."""
        return self.nome
    
class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
        
    def __str__(self):
        """String for representing the Model object."""
        return self.descricao + ' - ' + self.numero
    
