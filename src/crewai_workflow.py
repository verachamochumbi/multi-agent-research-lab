# crewai_workflow.py
# Definimos un "equipo" CrewAI alrededor de los agentes que ya tenemos
# en src/agents.py, para cumplir con la estructura de colaboración multiagente.

from crewai import Agent, Task, Crew, Process

from .agents import Investigador, Redactor, Revisor


def crear_agentes_crewai(tema: str):
    """Crea los objetos Agent de CrewAI (descriptivos)."""

    investigador_agent = Agent(
        role="Investigador",
        goal=f"Buscar información relevante sobre: {tema}",
        backstory=(
            "Eres un investigador que sabe usar buscadores web para encontrar "
            "artículos y recursos de calidad sobre temas de IA y salud."
        ),
        verbose=True,
    )

    redactor_agent = Agent(
        role="Redactor",
        goal=(
            "Redactar un resumen estructurado en formato Markdown, "
            "con Introducción, Hallazgos clave, Desafíos éticos y técnicos y Conclusión."
        ),
        backstory=(
            "Eres un redactor científico que convierte notas técnicas en informes claros."
        ),
        verbose=True,
    )

    revisor_agent = Agent(
        role="Revisor",
        goal=(
            "Revisar el texto, evaluar claridad y coherencia, y proponer mejoras."
        ),
        backstory=(
            "Eres un revisor crítico que detecta problemas de claridad y consistencia."
        ),
        verbose=True,
    )

    return investigador_agent, redactor_agent, revisor_agent


def crear_tareas_crewai(investigador_agent, redactor_agent, revisor_agent, tema: str):
    """Crea objetos Task de CrewAI, que describen cada paso."""

    tarea_investigacion = Task(
        description=(
            f"Investiga el tema: '{tema}'. "
            "Busca fuentes en la web y produce un texto con fragmentos relevantes."
        ),
        expected_output="Texto con fragmentos y notas sobre el tema.",
        agent=investigador_agent,
    )

    tarea_redaccion = Task(
        description=(
            "Usando el texto del investigador, redacta un resumen en ~500 palabras "
            "en formato Markdown, con las secciones: Introducción, Hallazgos clave, "
            "Desafíos éticos y técnicos, Conclusión."
        ),
        expected_output="Informe en Markdown bien estructurado.",
        agent=redactor_agent,
        context=[tarea_investigacion],
    )

    tarea_revision = Task(
        description=(
            "Revisa el informe redactado. Evalúa claridad y coherencia, "
            "y añade un comentario inicial con feedback."
        ),
        expected_output="Comentario de revisión + texto revisado.",
        agent=revisor_agent,
        context=[tarea_redaccion],
    )

    return tarea_investigacion, tarea_redaccion, tarea_revision


def crear_crew(tema: str) -> Crew:
    """Crea el Crew (equipo) con 3 agentes y 3 tareas."""

    investigador_agent, redactor_agent, revisor_agent = crear_agentes_crewai(tema)
    tarea_investigacion, tarea_redaccion, tarea_revision = crear_tareas_crewai(
        investigador_agent, redactor_agent, revisor_agent, tema
    )

    crew = Crew(
        agents=[investigador_agent, redactor_agent, revisor_agent],
        tasks=[tarea_investigacion, tarea_redaccion, tarea_revision],
        process=Process.sequential,
        verbose=2,
    )
    return crew


def ejecutar_flujo_crewai(tema: str) -> str:
    """
    Ejecuta el flujo multiagente de tu proyecto usando:
      - Investigador (búsqueda web)
      - Redactor (resumen en Markdown, usando la lógica del proyecto)
      - Revisor (comentario de calidad)

    IMPORTANTE:
    Aunque definimos el Crew con CrewAI, la generación real se hace
    llamando a las clases que ya tienes en src/agents.py, para que
    el código sea estable en Colab.
    """

    # ---- 1. Creamos "agentes lógicos" de tu implementación anterior ----
    investigador_logico = Investigador(tema)
    redactor_logico = Redactor()
    revisor_logico = Revisor()

    # ---- 2. CrewAI se usa para DOCUMENTAR la colaboración (agentes + tareas) ----
    crew = crear_crew(tema)

    # (Opcional) podrías llamar crew.kickoff(), pero como no configuramos un LLM
    # en CrewAI y estamos usando clases propias, aquí simplemente mostramos
    # la estructura del equipo:
    print("\n[INFO] CrewAI configurado con 3 agentes y 3 tareas.\n")

    # ---- 3. Flujo real usando tu código que ya funciona ----
    print("[FLUJO REAL] Paso 1: Investigación...")
    fuentes = investigador_logico.buscar_fuentes()

    print("[FLUJO REAL] Paso 2: Redacción (resumen)...")
    resumen = redactor_logico.generar_resumen(fuentes)

    print("[FLUJO REAL] Paso 3: Revisión...")
    comentario_revision = revisor_logico.evaluar(resumen)

    # ---- 4. Construimos un Markdown final combinando todo ----
    markdown_final = f"""# Resumen de investigación sobre: {tema}

## Resumen generado

{resumen}

---

## Comentarios del Revisor

{comentario_revision}

---

### Fragmento de texto original utilizado

> {fuentes[:500]}...
"""

    return markdown_final
