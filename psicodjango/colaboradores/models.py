from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from psicodjango.grupos.models import Grupo
from django.contrib.auth import get_user_model

class ColaboradorManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, cpf, password=None, **extra_fields):
        if not cpf:
            raise ValueError('O CPF deve ser informado')
        cpf = str(cpf)
        user = self.model(cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(cpf, password, **extra_fields)

# Create your models here.
class Colaborador(AbstractUser):
    username = None  # Remove o campo username padrão
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=255)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='colaboradores', null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['nome', 'sobrenome', 'email', 'data_nascimento']

    objects = ColaboradorManager()

    def __str__(self):
        return f"{self.nome} {self.sobrenome} ({self.cpf})"

class QuestionarioResposta(models.Model):
    colaborador = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='respostas_questionario')
    data_envio = models.DateTimeField(auto_now_add=True)
    # 20 campos para as respostas
    for i in range(1, 21):
        locals()[f'pergunta_{i}'] = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    del i

    def __str__(self):
        return f'Resposta de {self.colaborador} em {self.data_envio:%d/%m/%Y %H:%M}'
