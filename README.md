# Disciplina.me

Disciplina.me é um assistente acadêmico que ajuda a registrar aulas puladas, calcular a média de notas e muito mais para melhorar o desempenho dos alunos.

## 🛠️ Stack Tecnológico

- **Linguagem:** Python
- **Framework:** Django
- **Banco de Dados:** SQLite (padrão do Django)

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:
- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

Você pode verificar as versões instaladas com:
```bash
python --version
pip --version
```

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/juanzeen/Disciplina.me.git
cd Disciplina.me
```

### 2. Crie um ambiente virtual

É recomendado usar um ambiente virtual para isolar as dependências do projeto.

**No Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

**No Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

Instale todas as dependências com:

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Execute as migrações do Django para configurar o banco de dados:

```bash
python manage.py migrate
```

Este comando criará as tabelas necessárias no banco de dados SQLite.

### 5. Crie um superusuário (admin)

Para acessar o painel administrativo do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

Você será solicitado a informar:
- Nome de usuário
- Email
- Senha

## ▶️ Executando o projeto

### Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

O servidor estará disponível em: **http://127.0.0.1:8000/**

Se desejar rodar em uma porta específica:
```bash
python manage.py runserver 8080
```

### Acesse o painel administrativo

Navegue até **http://127.0.0.1:8000/admin** e faça login com as credenciais do superusuário criado anteriormente.

## 📝 Comandos úteis do Django

### Criar novas migrações

Após modificar os modelos, crie uma nova migração:
```bash
python manage.py makemigrations
```

### Aplicar migrações

```bash
python manage.py migrate
```

### Criar um novo app Django

```bash
python manage.py startapp nome_do_app
```

### Shell interativo

Para interagir com o banco de dados via shell Python:
```bash
python manage.py shell
```

### Resetar o banco de dados

Se precisar recriar o banco de dados do zero:
```bash
python manage.py flush
```

## 📦 Desativar o ambiente virtual

Quando terminar de trabalhar no projeto:

**No Linux/macOS:**
```bash
deactivate
```

**No Windows:**
```bash
deactivate
```

## 📞 Suporte

Para mais informações sobre Django, visite a [documentação oficial](https://docs.djangoproject.com/).

---

**Desenvolvido com ❤️**
