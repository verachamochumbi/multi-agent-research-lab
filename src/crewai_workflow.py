from crewai import Crew, Task
from src.crewai_agents import investigator, writer, reviewer

def ejecutar_flujo_crewai(prompt):
    # Definir tareas
    tarea_investigacion = Task(
        name="investigar",
        description=f"Investiga el siguiente tema y recupera texto relevante: {prompt}",
        agent=investigator
    )

    tarea_escritura = Task(
        name="escribir",
        description="Redacta un informe científico completo basado en los hallazgos.",
        agent=writer,
        requires=[tarea_investigacion]
    )

    tarea_revision = Task(
        name="revisar",
        description="Evalúa el informe y añade comentarios críticos.",
        agent=reviewer,
        requires=[tarea_escritura]
    )

    crew = Crew(
        agents=[investigator, writer, reviewer],
        tasks=[tarea_investigacion, tarea_escritura, tarea_revision],
        verbose=2
    )

    return crew.run()
