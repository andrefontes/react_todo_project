# Usando a imagem oficial do Node.js
FROM node:14

# Definindo o diretório de trabalho no contêiner
WORKDIR /app

# Copiando o package.json e package-lock.json
#COPY todo-frontend/package*.json /app/
#COPY todo-frontend/package*.json /app/
#COPY package*.json ./
#COPY package.json /app
COPY todo-frontend/package.json /app/
COPY todo-frontend/package-lock.json /app/
#COPY todo-frontend/package-lock.json /app/

# Instalando as dependências do Node.js
RUN npm install

# Copiando o restante do código da aplicação
#COPY . .
COPY todo-frontend /app
#COPY todo-frontend /app

# Build da aplicação React
RUN npm run build

# Expondo a porta usada pela aplicação
EXPOSE 3000

# Comando para rodar a aplicação
CMD ["npm", "start"]





