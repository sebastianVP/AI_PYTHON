import streamlit as st
import requests

# Configuración del servidor local
API_URL = "http://192.168.18.83:1234/v1/chat/completions"
MODEL_NAME = "gpt-oss-20b"

st.title("💬 Chat con Modelo Local")

# Área de texto para el usuario
user_input = st.text_input("Escribe tu mensaje:")

# Mantener historial de conversación en la sesión
if "messages" not in st.session_state:
    st.session_state.messages = []

# Enviar mensaje al modelo cuando el usuario presiona Enter
if st.button("Enviar") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    payload = {
        "model": MODEL_NAME,
        "messages": st.session_state.messages,
        "temperature": 0.7,
        "max_tokens": 512
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        model_reply = data["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": model_reply})
    except requests.exceptions.RequestException as e:
        st.error(f"Error al conectar con el modelo: {e}")

# Mostrar conversación
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**Tú:** {msg['content']}")
    else:
        st.markdown(f"**Modelo:** {msg['content']}")
