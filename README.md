
# React Todo Project

Este é um projeto para uma aplicação web de gerenciamento de tarefas, desenvolvida com React para o front-end e Django REST Framework para o back-end.

## Sumário
- [Descrição do Projeto](#descrição-do-projeto)
- [Instalação](#instalação)
- [Rodando o Projeto](#rodando-o-projeto)
- [Arquitetura](#arquitetura)
- [Decisões de Design](#decisões-de-design)
- [Testes](#testes)

## Descrição do Projeto

A aplicação permite o gerenciamento de tarefas, oferecendo funcionalidades como:
- **CRUD de Tarefas**
- **Autenticação de Usuários**
- **Marcar tarefas como concluídas ou pendentes**
- **Filtragem e Paginação de tarefas**
- **Interface responsiva utilizando React**
- **APIs criadas com Django REST Framework**

## Instalação

### Requisitos
- Node.js e npm (ou yarn)
- Python 3.8+
- Django
- Docker (opcional)

### Passos para Rodar

1. Clone o repositório:

    ```bash
    git clone https://github.com/andrefontes/react_todo_project.git
    ```

2. Instale as dependências do front-end:

    ```bash
    cd todo-frontend
    npm install
    ```

3. Instale as dependências do back-end:

    ```bash
    cd todo-backend
    pip install -r requirements.txt
    ```

4. Configure o banco de dados no back-end:

    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário:

    ```bash
    python manage.py createsuperuser
    ```

6. Inicie os servidores:

- INICIAR BACK-END
Ative o ambiente virtual:
No terminal, navegue até o diretório "todo_backend" onde estiver a pasta "venv"
    ```bash
    .\venv\Scripts\activate
    cd .\todo_backend\
    python manage.py runserver
    ```

CASO NÃO FUNCIONE ETAPAS ANTERIORES, FAÇA:

Instale o django-rest-knox:
    ```bash
    pip install django-rest-knox
    ```

Adicione o django-rest-knox ao requirements.txt:
    ```bash
    pip freeze > requirements.txt
    ```

Execute as migrações do Django: 
    ```bash
    python manage.py migrate
    ```
EXECUTE ETAPAS ANTERIORES

Acesse o aplicativo em: `http://localhost:8000/admin/`


- INICIAR FONT-END (na pasta `todo-frontend`)
    ```bash
    npm start
    ``` 
    

Acesse o aplicativo em: `http://127.0.0.1:3000/`
	


## Rodando com Docker (Opcional)

1. Crie os contêineres com Docker Compose:

    ```bash
    docker-compose up --build
    ```

## Arquitetura

A aplicação segue uma arquitetura baseada em:
- **React** para a interface do usuário, permitindo uma experiência dinâmica.
- **Django REST Framework** para a criação da API RESTful.
- **Docker** para containerização dos serviços (opcional).

## Decisões de Design

- **SOLID**: As funcionalidades foram organizadas para garantir boa manutenção e escalabilidade.
- **DRY**: O código é reutilizável, evitando duplicação de lógica.
- **KISS**: Manter o código simples e direto, focando na funcionalidade principal.

## Testes

### Testes Unitários

Certifique-se de que o `pytest` está instalado:

```bash
pip install pytest pytest-django
```

Para rodar os testes:

```bash
pytest
```

### Testes de Front-end (Selenium)

Testes de interface também podem ser realizados com Selenium.

## Contato

- **Autor**: [André Fontes](https://github.com/andrefontes)
