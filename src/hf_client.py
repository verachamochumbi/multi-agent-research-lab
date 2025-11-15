# hf_client.py
# Versión simple: usamos directamente la Inference API de Hugging Face con requests.

import os
import requests

# Token de Hugging Face (lo pones en Colab en os.environ["HF_TOKEN"])
HF_TOKEN = os.getenv("HF_TOKEN", None)

# Modelo de texto que SÍ soporta text-generation en la Inference API
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def generar_resumen_markdown(texto_fuente: str) -> str:
    """
    Llama directamente a la API de Hugging Face para generar
    un informe en Markdown (~500 palabras) con esta estructura:

    # Introducción
    ## Hallazgos clave
    ## Desafíos éticos y técnicos
    ## Conclusión
    """

    if HF_TOKEN is None:
        return "Error: no se encontró HF_TOKEN en las variables de entorno."

    texto_recortado = texto_fuente[:2000]

    prompt = f"""
Eres un asistente de investigación en IA.

A partir de las siguientes notas sobre el impacto de los datos sintéticos en la atención médica,
escribe un informe en ESPAÑOL de alrededor de 500 palabras, en FORMATO MARKDOWN, usando EXACTAMENTE
estas secciones y títulos:

# Introducción

## Hallazgos clave

## Desafíos éticos y técnicos

## Conclusión

No añadas otras secciones adicionales. Usa un tono claro y académico.

Notas de referencia:
\"\"\"{texto_recortado}\"\"\"
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 700,
            "temperature": 0.4,
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    try:
        response.raise_for_status()
    except Exception as e:
        return f"Error al llamar a la API de Hugging Face: {e}\nRespuesta: {response.text}"

    data = response.json()

    # Formato típico de la Inference API para text-generation:
    # [ { "generated_text": "..." } ]
    if isinstance(data, list) and len(data) > 0 and "generated_text" in data[0]:
        return data[0]["generated_text"]

    # Si la respuesta tiene otro formato, la devolvemos como texto.
    return str(data)
