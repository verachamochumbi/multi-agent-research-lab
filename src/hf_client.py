# hf_client.py
# Cliente para interactuar con la API de Hugging Face usando modo "chat".

import os
from huggingface_hub import InferenceClient

# Tomamos el token desde las variables de entorno (lo pones en Colab)
HF_TOKEN = os.getenv("HF_TOKEN", None)

# Creamos un cliente genérico (sin fijar tarea)
client = InferenceClient(token=HF_TOKEN)

MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta"
# Este modelo está pensado para uso conversacional, así que usamos chat_completion.

def generar_resumen_markdown(texto_fuente: str) -> str:
    """
    Usa un modelo de chat de Hugging Face para generar un informe en Markdown (~500 palabras),
    con la estructura:
    - Introducción
    - Hallazgos clave
    - Desafíos éticos y técnicos
    - Conclusión
    """

    texto_recortado = texto_fuente[:2000]

    system_message = (
        "Eres un asistente de investigación en IA. "
        "Genera un informe claro en español, en formato Markdown (~500 palabras), "
        "con las secciones: Introducción, Hallazgos clave, Desafíos éticos y técnicos, Conclusión."
    )

    user_message = f"Estas son las notas y fragmentos sobre el tema:\n\"\"\"{texto_recortado}\"\"\""

    completion = client.chat_completion(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        max_tokens=700,
        temperature=0.4,
    )

    # La respuesta viene en completion.choices[0].message["content"]
    return completion.choices[0].message["content"]
