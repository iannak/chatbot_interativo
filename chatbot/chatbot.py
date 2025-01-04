# chatbot/chatbot.py
from chatbot.grop_api import GroqLLM
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

groq_model = GroqLLM(api_key=API_KEY)

def iniciar_chatbot(user_input):
    response = groq_model.generate(user_input)
    return response
