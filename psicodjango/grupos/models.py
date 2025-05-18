from django.db import models
from empresas.models import Empresa

# Create your models here.

class Grupo(models.Model):
    nome = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='grupos')

    class Meta:
        unique_together = ('nome', 'empresa')
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return f"{self.nome} ({self.empresa.nome})"
