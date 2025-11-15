**🧠 Multi-Agent Research Lab**

_**Simulación de investigación colaborativa con CrewAI + Hugging Face**_

Este proyecto implementa un flujo de trabajo de colaboración multiagente, donde tres agentes autónomos (Investigador, Redactor y Revisor) trabajan juntos para producir un informe de investigación sobre un tema relacionado con la Inteligencia Artificial.

El sistema combina:

- CrewAI → coordinación y ejecución del equipo de agentes
- DuckDuckGo Search → recuperación de información
- Hugging Face Inference API → generación de texto y resúmenes
- Python 3.10+
- Estructura modular en src/

El objetivo es simular un laboratorio virtual de investigación, donde cada agente cumple un rol específico y se comunica con el resto para completar una tarea común.

**Integrantes**
- Vera Chamochumbi
- Fabrizio Sulca

  
**🧩 Descripción del flujo multiagente**

**🟦 1. Agente Investigador**
- Realiza búsquedas en la web usando DuckDuckGo
- Recupera fragmentos de texto relevantes
- Produce material de entrada para el redactor

**🟩 2. Agente Redactor**
- Utiliza Hugging Face Inference API
- Resume, limpia y estructura la información
- Produce un borrador del informe en formato Markdown

**🟨 3. Agente Revisor**
- Evalúa coherencia, claridad y factualidad
- Agrega sugerencias de mejora
- Devuelve retroalimentación al redactor

**🟥 4. CrewAI coordina la conversación**
- Los agentes se comunican entre sí mediante:
- Asignación de tareas
- Paso de información
- Ejecución secuenciada

El resultado final se almacena automáticamente como:

📄 research_summary.md


**📘 Tecnologías utilizadas**
| Tecnología                     | Uso                              |
| ------------------------------ | -------------------------------- |
| **CrewAI**                     | Coordinación multiagente         |
| **Hugging Face Inference API** | Generación de resúmenes y textos |
| **DuckDuckGo Search**          | Recuperación de información      |
| **Python 3.10+**               | Lenguaje principal               |
| **Google Colab**               | Entorno de ejecución             |

**🎯 Criterios de evaluación y cumplimiento**
| Criterio                                         | Cumplimiento |
| ------------------------------------------------ | ------------ |
| ✔ Configuración correcta (CrewAI + Hugging Face) | ✓            |
| ✔ Colaboración multiagente funcional             | ✓            |
| ✔ Agente Investigador recupera texto             | ✓            |
| ✔ Agente Redactor resume contenido               | ✓            |
| ✔ Agente Revisor analiza coherencia              | ✓            |
| ✔ Archivo final Markdown bien estructurado       | ✓            |

**📄 Resultado final**

El sistema genera automáticamente:

📁 research_summary.md
que contiene:
- Introducción
- Hallazgos clave
- Desafíos éticos y técnicos
- Conclusión

Todo generado, revisado y sintetizado por el equipo multiagente.
