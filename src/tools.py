# tools.py
# Herramientas que los agentes pueden usar.
# En esta versión usamos directamente la librería duckduckgo_search,
# sin depender de langchain_community.

from duckduckgo_search import DDGS

def buscar_en_web(query: str) -> str:
    """
    Busca información en DuckDuckGo y devuelve un texto con
    títulos y fragmentos de los resultados.
    """
    try:
        resultados_texto = []

        # DDGS es el cliente de búsqueda
        with DDGS() as ddgs:
            # max_results=5 para no traer demasiado
            for r in ddgs.text(query, max_results=5):
                titulo = r.get("title", "")
                cuerpo = r.get("body", "")
                link = r.get("href", "")
                resultados_texto.append(f"Título: {titulo}\nResumen: {cuerpo}\nLink: {link}\n")

        if not resultados_texto:
            return "No se encontraron resultados relevantes."

        return "\n\n".join(resultados_texto)

    except Exception as e:
        return f"Error al buscar en la web: {e}"
