# Disciplina.me

Disciplina.me é um assistente acadêmico projetado para ajudar alunos a gerenciarem seu desempenho, registrando aulas, calculando médias e organizando o calendário acadêmico.

O projeto foi reestruturado em uma **arquitetura de microserviços** para garantir escalabilidade e separação de responsabilidades.

## 🏗️ Arquitetura e Stack

O sistema é composto por três microserviços principais, todos desenvolvidos em **Python** com **Django**:

- **Auth Service:** Gerenciamento de usuários e autenticação (Porta 8001).
- **Calendar Service:** Gestão de calendários e eventos acadêmicos (Porta 8002).
- **Subjects Service:** Registro de matérias, notas e faltas (Porta 8003).

### Tecnologias:
- **Linguagens/Frameworks:** Python 3, Django
- **Banco de Dados:** PostgreSQL (uma base para cada serviço)
- **Containerização:** Docker & Docker Compose

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:
- **Docker**
- **Docker Compose**

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/juanzeen/Disciplina.me.git
cd Disciplina.me
```

### 2. Configure as Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis (exemplo):

```env
# Banco de Dados
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=db

# Nomes dos Bancos de Dados
AUTH_DB_NAME=disciplina_me_auth
CALENDAR_DB_NAME=disciplina_me_calendar
SUBJECTS_DB_NAME=disciplina_me_subjects

# Secret Keys para cada serviço
AUTH_SECRET_KEY=sua_chave_secreta_auth
CALENDAR_SECRET_KEY=sua_chave_secreta_calendar
SUBJECTS_SECRET_KEY=sua_chave_secreta_subjects

# Credenciais de super usuário padrão
DJANGO_SUPERUSER_USERNAME=seu_username
DJANGO_SUPERUSER_PASSWORD=sua_senha
DJANGO_SUPERUSER_EMAIL=seu_email
```

### 3. Suba os containers
Utilize o Docker Compose para construir e iniciar todos os serviços:

```bash
docker-compose up --build
```

Isso irá:
1. Iniciar o banco de dados PostgreSQL.
2. Criar os bancos de dados necessários através do script `init-db.sh`.
3. Rodar as migrações em cada microserviço.
4. Iniciar os servidores de desenvolvimento em suas respectivas portas.

## 🔗 Acesso aos Serviços

- **Auth Service:** [http://localhost:8001](http://localhost:8001)
- **Calendar Service:** [http://localhost:8002](http://localhost:8002)
- **Subjects Service:** [http://localhost:8003](http://localhost:8003)

Cada serviço possui seu próprio painel administrativo acessível via `/admin`.

## 📝 Comandos Úteis (Docker)

### Criar superusuário em um serviço específico
Para acessar o admin, você precisará de um superusuário em cada serviço:
```bash
docker-compose exec auth-service python manage.py createsuperuser
docker-compose exec calendar-service python manage.py createsuperuser
docker-compose exec subjects-service python manage.py createsuperuser
```

### Criar novas migrações
```bash
docker-compose exec <nome-do-servico> python manage.py makemigrations
```

### Executar novas migrações
```bash
docker-compose exec <nome-do-servico> python manage.py migrate
```

### Ver Logs
```bash
docker-compose logs -f
```

## 📞 Suporte

Para mais informações sobre a stack utilizada, visite a [documentação oficial do Django](https://docs.djangoproject.com/) e do [Docker](https://docs.docker.com/).
