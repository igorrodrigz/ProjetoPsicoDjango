from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Colaborador

def formatar_data_nascimento(data_nascimento):
    return data_nascimento.strftime('%d%m%Y')

@receiver(post_save, sender=Colaborador)
def criar_login_senha(sender, instance, created, **kwargs):
    if created:
        # Garante que o CPF está sem pontuação
        instance.cpf = ''.join(filter(str.isdigit, instance.cpf))
        # Define a senha como data de nascimento formatada
        senha = formatar_data_nascimento(instance.data_nascimento)
        instance.set_password(senha)
        instance.save()
