from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    mensagem = models.TextField()
    receber_noticias = models.BooleanField()
    
    def __str__(self):
        return self.nome
