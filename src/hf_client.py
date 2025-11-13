# hf_client.py
# Cliente para interactuar con la API de Hugging Face e invocar modelos para resumir.

import os
from huggingface_hub import InferenceClient

# Tomamos el token que guardaste en Colab
HF_TOKEN = os.getenv("HF_TOKEN", None)

# Modelo elegido (puedes cambiarlo luego si quieres)
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

# Creamos el cliente de inferencia
client = InferenceClient(model=MODEL_NAME, token=HF_TOKEN)

def generar_resumen_markdown(texto_fuente: str) -> str:
    """
    Genera un resumen estructurado en Markdown (~500 palabras)
    usando un modelo de Hugging Face.
    """

    texto_recortado = texto_fuente[:2000]  # evita que el prompt sea demasiado largo

    prompt = f"""
Eres un asistente de investigación en IA.

A partir de las siguientes notas, genera un informe en español (~500 palabras),
con formato Markdown y esta estructura:

# Introducción

## Hallazgos clave

## Desafíos éticos y técnicos

## Conclusión

Notas de referencia:
\"\"\"{texto_recortado}\"\"\"
"""

    # Llamada al modelo
    respuesta = client.text_generation(
        prompt,
        max_new_tokens=700,
        temperature=0.4,
    )

    return respuesta
