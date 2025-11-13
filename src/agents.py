# agents.py
# Versión súper simple de los agentes, para entender el flujo.
# Más adelante los convertiremos en agentes "de verdad" con CrewAI y Hugging Face.

from .tools import buscar_en_web


class Investigador:
    def __init__(self):
        self.nombre = "Agente Investigador"

    def actuar(self, tema):
        """Busca información en la web sobre un tema y devuelve el texto encontrado."""
        consulta = f"{tema} impacto datos sintéticos en salud"
        print(f"[{self.nombre}] Buscando en la web sobre: {consulta}")
        resultados = buscar_en_web(consulta)
        return resultados


class Escritor:
    def __init__(self):
        self.nombre = "Agente Escritor"

    def actuar(self, texto_fuente):
        """Crea un mini-resumen de prueba (sin IA todavía)."""
        print(f"[{self.nombre}] Escribiendo un borrador de resumen...")
        # De momento, solo devolvemos las primeras líneas como "borrador"
        borrador = (
            "# Resumen preliminar\n\n"
            "Este es un borrador muy simple basado en la información encontrada.\n\n"
            "Fragmento usado:\n\n"
            f"{texto_fuente[:500]}\n"
        )
        return borrador


class Revisor:
    def __init__(self):
        self.nombre = "Agente Revisor"

    def actuar(self, borrador):
        """Simula una revisión muy básica del texto."""
        print(f"[{self.nombre}] Revisando el borrador...")
        comentario = (
            "Comentario del revisor: El texto necesita más estructura, "
            "pero por ahora lo aceptamos como borrador inicial.\n\n"
        )
        version_revisada = comentario + borrador
        return version_revisada


def ejecutar_flujo_simple(tema):
    """Orquesta el flujo: Investigador → Escritor → Revisor."""
    investigador = Investigador()
    escritor = Escritor()
    revisor = Revisor()

    texto = investigador.actuar(tema)
    borrador = escritor.actuar(texto)
    resumen_final = revisor.actuar(borrador)

    return resumen_final
