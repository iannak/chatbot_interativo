# Usando uma imagem base do Python
FROM python:3.9-slim

# Definir diretório de trabalho
WORKDIR /app

# Definir variáveis de ambiente (exemplo: chave de API do OpenAI ou Groq)
ENV OPENAI_API_KEY="sua_chave_de_api_openai_ou_groq"

# Copiar os arquivos do código para o container
COPY . /app

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta para o Streamlit
EXPOSE 8501

# Rodar o aplicativo Streamlit
CMD ["streamlit", "run", "app.py"]
