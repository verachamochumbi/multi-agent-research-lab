🧠 Multi-Agent Research Lab
Laboratorio de Investigación en IA con Agentes Colaborativos

Este repositorio contiene mi implementación del Ejercicio 1 del laboratorio “Colaboración Multiagente + Razonamiento RAG”.
El objetivo es simular un pequeño laboratorio virtual de IA, donde varios agentes autónomos trabajan juntos para producir un informe de investigación.

🎯 Objetivo del laboratorio

Crear un flujo de trabajo multiagente donde:

Un Agente Investigador busca información en la web.

Un Agente Escritor genera un resumen estructurado en Markdown.

Un Agente Revisor evalúa la coherencia del texto y agrega comentarios.

Finalmente, el sistema produce un archivo:
research_summary.md
con la estructura requerida:

Introducción

Hallazgos clave

Desafíos éticos y técnicos

Conclusión

🏗️ Estructura del repositorio
multi-agent-research-lab/
│
├── src/
│   ├── agents.py        → Lógica del Investigador, Escritor y Revisor
│   ├── tools.py         → Búsqueda web (DuckDuckGo Search)
│   ├── hf_client.py     → Cliente para generar el resumen (versión local)
│
├── data/                → (Carpeta reservada para datos si se requieren)
│
├── notebooks/
│   ├── workflow_demo.ipynb   → Notebook demostrando la ejecución completa
│
├── research_summary.md  → Informe final generado por el sistema
├── requirements.txt     → Dependencias del proyecto
└── README.md            → Este archivo

🧩 Descripción de los agentes
🔍 Agente Investigador

Recibe un tema de investigación.

Ejecuta una búsqueda web usando DuckDuckGo Search.

Devuelve fragmentos de texto o mensajes relevantes.

✍️ Agente Escritor

Toma la información recopilada por el Investigador.

Genera un informe en formato Markdown, siguiendo la estructura del laboratorio.

Debido a cambios recientes en la API Inference de Hugging Face, este repositorio incluye una versión local de generación de resumen (sin depender de una API externa), manteniendo el flujo funcional.

✔️ Agente Revisor

Lee el borrador generado por el Escritor.

Añade un comentario evaluando claridad y coherencia.

🔁 Flujo de trabajo

El usuario ejecuta el flujo con un tema, por ejemplo:

ejecutar_flujo_simple("Impacto de los datos sintéticos en la atención médica")


El Investigador busca información en línea.

El Escritor usa esa información para generar un informe.

El Revisor analiza el texto y produce un comentario.

El sistema devuelve el Markdown final.

Ese texto se guarda como research_summary.md.

📓 Notebook de demostración

El archivo:

notebooks/workflow_demo.ipynb


muestra paso a paso:

Importación de dependencias

Ejecución del flujo multiagente

Resultado final del informe

Guardado del archivo Markdown

Está pensado para ser corrido en Google Colab.

📄 Archivo final generado

El resultado de todo el flujo se encuentra en:

research_summary.md


Este archivo contiene el informe estructurado con todos los apartados requeridos.

⚙️ Requerimientos

El entorno puede configurarse instalando las dependencias desde:

requirements.txt

📝 Notas técnicas

Este proyecto está diseñado de forma modular para facilitar ser extendido a versiones más avanzadas con CrewAI o integración real con la Hugging Face Inference API.

Debido a cambios recientes en los endpoints oficiales de HuggingFace, el cliente incluído (hf_client.py) funciona en modo local para mantener la ejecución estable en Google Colab.

🎓 Conclusión

Este laboratorio demuestra cómo varios agentes especializados pueden colaborar para resolver una tarea de investigación automatizada.
El flujo funciona de inicio a fin y produce un informe estructurado listo para ser evaluado.

Siéntete libre de explorar los agentes, ajustar el resumen o integrar nuevas herramientas.
