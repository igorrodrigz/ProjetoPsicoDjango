# PsicoDjango

Sistema de gestão para empresas clientes, grupos e colaboradores, com questionário e relatórios.

## Funcionalidades
- Cadastro de empresas, grupos e colaboradores
- Login de colaboradores usando CPF e senha
- Cadastro e autenticação via Django Admin
- Questionário com 20 perguntas (sim/não) para colaboradores
- Armazenamento das respostas no banco de dados
- Relatórios e visualização das respostas no admin
- Geração de gráficos e exportação para PDF (em desenvolvimento)

## Instalação
1. Clone o repositório e acesse a pasta do projeto:
   ```sh
   git clone <repo-url>
   cd psicodjango
   ```
2. Crie e ative o ambiente virtual:
   ```sh
   python -m venv psicoenv
   psicoenv\Scripts\activate
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Rode as migrações:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Crie um superusuário:
   ```sh
   python manage.py createsuperuser
   ```
6. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```

## Uso
- Acesse `/admin/` para gerenciar empresas, grupos e colaboradores.
- Colaboradores podem acessar `/colaboradores/login/` para login e `/colaboradores/index/` para acessar funcionalidades.
- O questionário está disponível em `/colaboradores/questionario/`.

## Relatórios
- As respostas dos questionários podem ser visualizadas e exportadas pelo admin.
- Geração de relatórios em PDF com gráficos será implementada usando Matplotlib e ReportLab.

## Estrutura dos Apps
- `empresas/`: Cadastro de empresas
- `grupos/`: Cadastro de grupos vinculados a empresas
- `colaboradores/`: Cadastro de colaboradores, autenticação, questionário e relatórios

## Licença
MIT
