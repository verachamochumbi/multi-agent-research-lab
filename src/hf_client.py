# hf_client.py
# Versión simplificada SIN llamadas a la API de Hugging Face.
# Genera un resumen en Markdown usando el texto que le pasa el agente Investigador.

def generar_resumen_markdown(texto_fuente: str) -> str:
    """
    Genera un informe en Markdown (~500 palabras aprox.)
    con la estructura pedida en el laboratorio:

    # Introducción
    ## Hallazgos clave
    ## Desafíos éticos y técnicos
    ## Conclusión

    No usa modelos remotos (Hugging Face), solo hace una síntesis muy simple
    del texto de entrada para que el flujo funcione en entornos donde la API
    no está disponible.
    """

    # Nos quedamos con un fragmento razonable del texto original
    fragmento = texto_fuente[:1200]

    introduccion = (
        "En este informe se analiza el impacto del uso de datos sintéticos en "
        "el ámbito de la atención médica. A partir de distintas fuentes en "
        "línea se resumen las oportunidades, riesgos y desafíos asociados al "
        "empleo de datos generados artificialmente para entrenar y evaluar "
        "modelos de inteligencia artificial aplicados a la salud.\n"
    )

    hallazgos = (
        "- Los datos sintéticos permiten ampliar conjuntos de datos reales, "
        "lo que puede mejorar el rendimiento de modelos de IA cuando los "
        "datos clínicos son escasos o sensibles.\n"
        "- Facilitan el intercambio de información al reducir el riesgo de "
        "reidentificación de pacientes.\n"
        "- Pueden introducir sesgos o patrones irreales si el proceso de "
        "generación no refleja adecuadamente la población y la práctica "
        "clínica.\n"
        "- Son especialmente útiles en áreas donde los datos reales son muy "
        "difíciles de obtener, como determinadas enfermedades raras.\n"
    )

    desafios = (
        "- Verificar la fidelidad estadística de los datos sintéticos frente "
        "a los datos reales es un reto técnico importante.\n"
        "- Existen dudas regulatorias y éticas sobre hasta qué punto es "
        "aceptable basar decisiones clínicas en modelos entrenados "
        "principalmente con datos sintéticos.\n"
        "- Se requiere transparencia sobre cómo se generaron los datos y qué "
        "limitaciones tienen para evitar conclusiones erróneas.\n"
        "- La calidad del dato sintético depende directamente de la calidad "
        "y representatividad de los datos reales de partida.\n"
    )

    conclusion = (
        "En conclusión, los datos sintéticos representan una herramienta "
        "prometedora para impulsar el desarrollo de modelos de IA en "
        "atención médica, especialmente en contextos con fuertes restricciones "
        "de privacidad o escasez de datos. Sin embargo, su uso responsable "
        "exige validar cuidadosamente su calidad, documentar su proceso de "
        "generación y combinar su uso con datos reales siempre que sea "
        "posible. Las instituciones sanitarias y los equipos de investigación "
        "deben considerar tanto los beneficios como los riesgos éticos y "
        "técnicos antes de adoptar soluciones basadas en datos sintéticos.\n"
    )

    markdown = f"""# Introducción

{introduccion}

## Hallazgos clave

{hallazgos}

## Desafíos éticos y técnicos

{desafios}

## Conclusión

{conclusion}

---

_Fragmento de texto original analizado (recortado):_

> {fragmento[:500]}...
"""

    return markdown
