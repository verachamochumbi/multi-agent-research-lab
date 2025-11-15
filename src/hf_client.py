# hf_client.py
# Cliente sencillo para la nueva API de Hugging Face (router.huggingface.co)
# usando el endpoint de chat completions compatible con OpenAI.

import os
import requests

HF_TOKEN = os.getenv("HF_TOKEN", None)

# Modelo: usa uno que sea de lenguaje general y esté disponible en HF Inference.
# Puedes cambiarlo por otro si lo deseas.
MODEL_PROVIDER = "deepseek-ai"
MODEL_ID = "DeepSeek-R1-Distill-Qwen-32B"

# URL según la documentación del router de Hugging Face:
# https://router.huggingface.co/hf-inference/models/:provider/:model_id/v1/chat/completions :contentReference[oaicite:1]{index=1}
API_URL = (
    f"https://router.huggingface.co/hf-inference/models/"
    f"{MODEL_PROVIDER}/{MODEL_ID}/v1/chat/completions"
)


def generar_resumen_markdown(texto_fuente: str) -> str:
    """
    Llama al router de Hugging Face para generar un informe en Markdown (~500 palabras)
    con las secciones:
      - Introducción
      - Hallazgos clave
      - Desafíos éticos y técnicos
      - Conclusión
    """

    if HF_TOKEN is None:
        return "Error: no se encontró HF_TOKEN en las variables de entorno."

    texto_recortado = texto_fuente[:2000]

    system_message = (
        "Eres un asistente de investigación en IA. "
        "Genera un informe claro en ESPAÑOL, en formato Markdown (~500 palabras), "
        "usando EXACTAMENTE estas secciones y títulos en este orden:\n\n"
        "# Introducción\n"
        "## Hallazgos clave\n"
        "## Desafíos éticos y técnicos\n"
        "## Conclusión\n\n"
        "No añadas secciones extra y no cambies los títulos."
    )

    user_message = (
        "Estas son notas y fragmentos recuperados de la web sobre el tema. "
        "Úsalas como referencia para escribir el informe final:\n\n"
        f"\"\"\"{texto_recortado}\"\"\""
    )

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        "max_tokens": 700,
        "stream": False,
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if not response.ok:
        return f"Error al llamar a la API de Hugging Face: {response.status_code} - {response.text}"

    data = response.json()

    # Formato OpenAI-like:
    # { "choices": [ { "message": { "role": "assistant", "content": "..." } } ] }
    try:
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error al interpretar la respuesta de HF: {e}\nRespuesta completa: {data}"
