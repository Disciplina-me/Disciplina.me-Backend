# Disciplina.me

Disciplina.me é um assistente acadêmico projetado para ajudar alunos a gerenciarem seu desempenho, registrando aulas, calculando médias e organizando o calendário acadêmico.

## 🏗️ Arquitetura e Stack

O sistema agora opera como um único projeto Django estruturado em módulos independentes (na pasta `apps/`):

- **Auth / Usuários:** Gerenciamento de usuários, autenticação e perfis customizados.
- **Calendar:** Gestão de calendários e eventos acadêmicos.
- **Subjects:** Registro de matérias, notas e faltas.

### Tecnologias:
- **Linguagens/Frameworks:** Python 3, Django, Django Rest Framework (DRF)
- **Banco de Dados:** PostgreSQL (Base de dados única unificada)
- **Containerização:** Docker & Docker Compose

## 📋 Pré-requisitos
cace
Antes de começar, certifique-se de ter instalado:
- **Docker**
- **Docker Compose**

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório
```bash
git clone [https://github.com/juanzeen/Disciplina.me.git](https://github.com/juanzeen/Disciplina.me.git)
cd Disciplina.me
```

### 2. Configure as variáveis de ambiente
```bash
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=db
DB_NAME=disciplina_me_db
SECRET_KEY=sua_chave_secreta_django
ALLOWED_HOSTS="localhost,127.0.0.1"

# Credenciais de super usuário padrão (Opcional, útil para scripts de inicialização)
DJANGO_SUPERUSER_EMAIL=seu_email@exemplo.com
DJANGO_SUPERUSER_PASSWORD=sua_senha
```

### 3. Suba os containers
`docker compose up --build`

1. Esse comando inicia o banco de dados PostgreSQL;
2. Aplica as migracões automaticamente;
3. Inicia o servidor de dev na porta 8000

### 4. Acessando o sistema
- API http://localhost:8080
- Django Admin http://localhost:8080/admin

### 5. Comandos utilitários do Docker

#### Criando super user
`docker compose exec web python manage.py createsuperuser`

#### Criando novas migracões
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py makemigrations calendar
```

#### Executando migracoes
`docker compose exec web python manage.py migrate`

#### Visualizar logs
`docker compose logs -f`
