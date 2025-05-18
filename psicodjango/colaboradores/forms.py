from django import forms
from .models import Colaborador
from django.core.exceptions import ValidationError
import re

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'data_nascimento', 'cpf', 'cidade', 'estado', 'cep', 'endereco', 'grupo']

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        cpf = re.sub(r'\D', '', cpf)  # Remove qualquer pontuação
        if len(cpf) != 11:
            raise ValidationError('O CPF deve conter 11 dígitos.')
        return cpf
