# Usando uma imagem base do Python
FROM python:3.9-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar os arquivos do código para o container
COPY . /app

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta para o Streamlit
EXPOSE 8501

# Rodar o aplicativo Streamlit
CMD ["streamlit", "run", "app.py"]
