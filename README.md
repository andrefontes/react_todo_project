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

Em caso de erro, faça (No PowerShell):

   ```bash
   Remove-Item -Recurse -Force .\venv
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
==> Tente os passos anteriores novamente



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

1. Executar Docker:

Para garantir que o Dockerfile e o docker-compose.yml funcionem corretamente, é recomendável parar quaisquer instâncias do backend e frontend que estejam rodando fora do Docker. Isso evita conflitos de portas e garante que os containers Docker possam iniciar sem problemas.

Para encerrar todos os processos que estão utilizando as portas 8000 e 3000 de uma vez só (geralmente com Ctrl + C no terminal):

porta 8000 (back-end)

   ```bash
   Get-NetTCPConnection -LocalPort 8000 | ForEach-Object {Stop-Process -Id $_.OwningProcess -Force}
   ```

porta 3000 (front-end)

   ```bash
   Get-NetTCPConnection -LocalPort 3000 | ForEach-Object {Stop-Process -Id $_.OwningProcess -Force}
   ```



Navegue até o diretório do projeto onde o `docker-compose.yml` está localizado:

Construir os Containers:
   ```bash
   docker-compose build
   ```

Iniciar os Containers:
   ```bash
   docker-compose up
   ```


CRIAR UM SUPERUSUÁRIO:

Se ainda não criou nenhum usuário, você pode criar um superusuário que pode ser usado para testes e administração. No diretório do backend, execute:

   ```bash
   python manage.py createsuperuser
   ```
=> Siga as instruções para definir um nome de usuário, e-mail e senha.

1 - Acesse a interface de administração do Django em http://127.0.0.1:8000/admin.

2 - Faça login com o superusuário que você criou.

31 - Navegue até a seção de usuários e crie um novo usuário, definindo o nome de usuário e a senha.



### Testes de Front-end (Selenium)

Testes de interface também podem ser realizados com Selenium.

1. Instalar Selenium e WebDriver. 
Navegue até a pasta do front-end (todo-frontend) e instale o Selenium:

   ```bash
   npm install selenium-webdriver
   ```

2. Executando o Teste. 
Certifique-se de que o servidor front-end esteja em execução (npm start dentro de todo-frontend). Então, execute o teste:

   ```bash
   node tests/todo.test.js
   ```

2. Executar os testes com:

   ```bash
   npm run test:selenium
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



## Contato

- **Autor**: [André Fontes](https://github.com/andrefontes)
