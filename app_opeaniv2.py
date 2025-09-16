import streamlit as st
import requests

# =============================
# CONFIGURACIÓN DEL SERVIDOR
# =============================
API_URL = "http://192.168.18.83:1234/v1/chat/completions"  # Cambia por tu IP
MODEL_NAME = "gpt-oss-20b"

# =============================
# CONFIGURACIÓN DE LA PÁGINA
# =============================
st.set_page_config(page_title="Chat Local LLM", layout="wide")
st.title("💬 Chat con Modelo Local")

# =============================
# BOTÓN PARA REINICIAR CONVERSACIÓN
# =============================
if st.button("🔄 Reiniciar conversación"):
    st.session_state.messages = []

# =============================
# INICIALIZAR HISTORIAL
# =============================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =============================
# MOSTRAR HISTORIAL ARRIBA
# =============================
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**Tú:** {msg['content']}")
    else:
        st.markdown(f"**Modelo:** {msg['content']}")

st.markdown("---")  # Separador visual

# =============================
# INPUT DEL USUARIO Y BOTÓN
# =============================
user_input = st.text_input("Escribe tu mensaje:")

if st.button("Enviar") and user_input:
    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Preparar payload
    payload = {
        "model": MODEL_NAME,
        "messages": st.session_state.messages,
        "temperature": 0.7,
        "max_tokens": 512
    }

    # Llamar al servidor local
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        data = response.json()

        # Compatibilidad con llama-server y OpenAI API
        model_reply = data["choices"][0].get("message", {}).get("content") or data["choices"][0].get("text", "")

        # Agregar respuesta al historial
        st.session_state.messages.append({"role": "assistant", "content": model_reply})

    except requests.exceptions.RequestException as e:
        st.error(f"Error al conectar con el modelo: {e}")
