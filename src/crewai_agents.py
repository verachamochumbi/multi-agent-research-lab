from crewai import Agent
from crewai_tools import DuckDuckGoSearchTool

search_tool = DuckDuckGoSearchTool()

investigator = Agent(
    role="Investigador",
    goal="Buscar información real y confiable sobre temas médicos o científicos.",
    backstory="Experto en búsqueda avanzada y verificación de fuentes.",
    tools=[search_tool],
    verbose=True
)

writer = Agent(
    role="Escritor Científico",
    goal="Redactar informes claros, estructurados y basados en los hallazgos.",
    backstory="Especialista en generar texto académico de alta calidad.",
    llm="huggingface/mistralai/Mistral-7B-Instruct-v0.2"
)

reviewer = Agent(
    role="Revisor",
    goal="Verificar claridad, coherencia y riesgos de factualidad.",
    backstory="Investigador crítico y meticuloso.",
    verbose=True
)
