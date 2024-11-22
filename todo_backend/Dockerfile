# Usando a imagem oficial do Python slim
FROM python:3.9-slim

# Definindo o diretório de trabalho no contêiner
WORKDIR /app

# Copiando o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instalando as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante do código da aplicação
COPY . .

# Comando para rodar a aplicação
CMD ["python", "todo_backend/manage.py", "runserver", "0.0.0.0:8000"]
