# Usa uma imagem base oficial do Python
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o requirements.txt para instalar as dependências
COPY requirements.txt .

# Instala as dependências do Flask
RUN pip install --no-cache-dir -r requirements.txt

# Cria o diretório para armazenar o banco SQLite
RUN mkdir -p /app/data

RUN mkdir -p /app/log

# Copia o restante do código da aplicação para o container
COPY . .

EXPOSE 8080

# Define o comando de inicialização
CMD ["flask", "run", "--host=0.0.0.0"]
