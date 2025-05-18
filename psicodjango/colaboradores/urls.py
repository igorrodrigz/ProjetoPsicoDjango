from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.criar_colaborador, name='criar_colaborador'),
    path('sucesso/', views.colaborador_sucesso, name='colaborador_sucesso'),
    path('login/', LoginView.as_view(template_name='colaboradores/login.html', next_page='index_colaborador'), name='login_colaborador'),
    path('logout/', LogoutView.as_view(next_page='login_colaborador'), name='logout_colaborador'),
    path('index/', views.index_colaborador, name='index_colaborador'),
    path('questionario/', views.questionario_colaborador, name='questionario_colaborador'),
]
