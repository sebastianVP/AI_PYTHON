# pip install openai
from openai import OpenAI

# ⚡ Reemplaza TU_IP y PUERTO por tu servidor LM Studio
client = OpenAI(
    base_url="http://10.10.10.28:1234/v1",
    api_key="lm-studio"   # Puede ser cualquier string, LM Studio no valida la API key
)

# Ejemplo de chat
response = client.chat.completions.create(
    model="openai/gps-pss-20b",
    messages=[
        {"role": "system", "content": "Eres un asistente útil"},
        {"role": "user", "content": "Explica la teoría de grafos en términos simples"}
    ]
)

print(response.choices[0].message.content)
