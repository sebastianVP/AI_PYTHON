import requests

url = "http://25.38.234.200:1234/v1/chat/completions"

data = {
    "model": "openai/gps-pss-20b",
    "messages": [
        {"role": "system", "content": "Eres un asistente útil"},
        {"role": "user", "content": "Dame un resumen de la teoría de grafos"}
    ]
}
response = requests.post(url, json=data)
print(response.json())
