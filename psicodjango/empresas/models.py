from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome