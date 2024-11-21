# Todo Backend Project

Este é um projeto backend para um aplicativo de lista de tarefas, desenvolvido com Django e Django Rest Framework.

## Sumário

- [Instalação](#instalação)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Rodando o Projeto](#rodando-o-projeto)
- [Testes](#testes)
- [Arquitetura](#arquitetura)
- [Decisões de Design](#decisões-de-design)

## Instalação

### Pré-requisitos

- Python 3.8+
- Pipenv (opcional, mas recomendado)

### Passos

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio/todo_project
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    .\venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure o banco de dados:
    ```sh
    python manage.py migrate
    ```

5. Crie um superusuário para acessar o admin do Django:
    ```sh
    python manage.py createsuperuser
    ```

## Configuração do Ambiente

1. Certifique-se de que as variáveis de ambiente estejam configuradas corretamente. Um exemplo de arquivo `.env` pode ser assim:
    ```
    DEBUG=True
    SECRET_KEY=sua-chave-secreta
    DATABASE_URL=sqlite:///db.sqlite3
    ```

2. Crie o arquivo `.env` na raiz do projeto e adicione as variáveis de ambiente conforme necessário.

## Rodando o Projeto

1. Ative o ambiente virtual, se ainda não estiver ativado:
    ```sh
    source venv/bin/activate  # Linux/MacOS
    .\venv\Scripts\activate  # Windows
    ```

2. Inicie o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

3. Acesse o aplicativo em `http://127.0.0.1:8000/`.

## Testes

### Instalando Pytest

Certifique-se de que o `pytest` está instalado:
```sh
pip install pytest pytest-django
