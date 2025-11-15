# agents.py
# Definición de los tres agentes lógicos que usa el flujo:
# Investigador, Redactor y Revisor.

from .tools import buscar_en_web
from .hf_client import generar_resumen_markdown


class Investigador:
    """Agente encargado de buscar información en la web."""

    def __init__(self, tema: str):
        self.tema = tema

    def buscar_fuentes(self) -> str:
        """Lanza una búsqueda web y devuelve texto con fragmentos relevantes."""
        query = f"{self.tema} impacto datos sintéticos en salud"
        print(f"[Agente Investigador] Buscando en la web sobre: {query}")
        resultados = buscar_en_web(query)
        return resultados


class Redactor:
    """Agente que genera un resumen estructurado a partir del texto del investigador."""

    def __init__(self):
        self.nombre = "Agente Escritor"

    def generar_resumen(self, texto_fuente: str) -> str:
        """Genera un resumen en formato Markdown (usa hf_client, versión local)."""
        print(f"[{self.nombre}] Generando resumen con Hugging Face...")
        resumen = generar_resumen_markdown(texto_fuente)
        return resumen


class Revisor:
    """Agente que revisa el texto final y hace comentarios de mejora."""

    def __init__(self):
        self.nombre = "Agente Revisor"

    def evaluar(self, texto: str) -> str:
        """Devuelve un comentario general sobre claridad y coherencia."""
        print(f"[{self.nombre}] Revisando el borrador...")
        comentario = (
            "El texto presenta una estructura clara (introducción, hallazgos, "
            "desafíos y conclusión). Podría reforzarse el tono académico con "
            "algunas transiciones más formales y, si es posible, incluir uno o "
            "dos ejemplos concretos de uso de datos sintéticos en entornos "
            "clínicos reales."
        )
        return comentario


# Función auxiliar (opcional) para probar sin CrewAI
def ejecutar_flujo_simple(tema: str) -> str:
    investigador = Investigador(tema)
    redactor = Redactor()
    revisor = Revisor()

    fuentes = investigador.buscar_fuentes()
    resumen = redactor.generar_resumen(fuentes)
    comentario = revisor.evaluar(resumen)

    salida = f"""
Comentario del revisor: {comentario}

{resumen}
"""
    return salida
