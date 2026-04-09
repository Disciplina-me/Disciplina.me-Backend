# 1. Imagem base (Python 3.12 leve)
FROM python:3.12-slim

# 2. Variáveis de ambiente para o Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Diretório de trabalho dentro do container
WORKDIR /app

# 4. Dependências do sistema para o PostgreSQL (essencial!)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# 5. Instalação das dependências do Python
# DICA: Garante que o arquivo requirements.txt esteja dentro da pasta do microserviço
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copia o código do microserviço
COPY . /app/

# 7. Expõe a porta interna (8000)
EXPOSE 8000
# 8. Comando para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
