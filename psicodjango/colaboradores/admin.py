from django.contrib import admin
from .models import Colaborador, QuestionarioResposta

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'sobrenome', 'email', 'grupo', 'is_staff')
    search_fields = ('cpf', 'nome', 'sobrenome', 'email')
    list_filter = ('grupo', 'is_staff')

@admin.register(QuestionarioResposta)
class QuestionarioRespostaAdmin(admin.ModelAdmin):
    list_display = ('colaborador', 'data_envio')
    search_fields = ('colaborador__cpf', 'colaborador__nome', 'colaborador__sobrenome')
    list_filter = ('data_envio',)

# Register your models here.
