# tools.py
# Este archivo contiene herramientas que los agentes pueden usar.
# Por ahora solo tendremos la herramienta de búsqueda web.

from langchain_community.tools import DuckDuckGoSearchRun

# Herramienta de búsqueda (la usará el investigador)
search_tool = DuckDuckGoSearchRun()

def buscar_en_web(query):
    """Función simple para buscar información en línea usando DuckDuckGo."""
    try:
        resultados = search_tool.run(query)
        return resultados
    except Exception as e:
        return f"Error al buscar: {e}"
