from django.apps import AppConfig


class ColaboradoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'psicodjango.colaboradores'

    def ready(self):
        import psicodjango.colaboradores.signals
