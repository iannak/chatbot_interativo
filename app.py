# app.py
import streamlit as st
from chatbot.chatbot import iniciar_chatbot
from chatbot.utils import preprocess_input, postprocess_output

# Título da aplicação
st.title("Chatbot Interativo com Groq")

# Caixa de texto para o input do usuário
user_input = st.text_input("Digite sua pergunta:")

# Verificar se o usuário digitou algo
if user_input:
    processed_input = preprocess_input(user_input)
    # Interagir com o chatbot
    response = iniciar_chatbot(processed_input)
    processed_response = postprocess_output(response)
    # Exibir a resposta do chatbot
    st.write("Resposta do Chatbot:", processed_response)
