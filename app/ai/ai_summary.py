import os
from google import genai

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

client = genai.Client(
        vertexai=True,
        project="psicopanel-495600",
        location="us-west1",
    )
def summarize_text(text: str):
    if not text:
        return ""
    
    try:

        prompt = f"""
        Analiza el siguiente texto extraído de una historia clínica psicológica y organiza la información de forma clara, profesional y legible.

        INSTRUCCIONES:
        - Corrige errores de OCR, ortografía y puntuación cuando sea posible.
        - Mantén el contenido original sin inventar información.
        - Resume únicamente la información relevante.
        - Separa la información en párrafos cortos y secciones claras.
        - Si un dato no está presente, no lo inventes.
        - Usa español profesional y claro.

        Extrae y organiza, si están presentes, los siguientes puntos:

        1. Motivo de consulta
        2. Posibles diagnósticos
        3. Síntomas principales
        4. Tratamientos anteriores
        5. Medicación mencionada
        6. Enfermedades o antecedentes relevantes
        7. Grupo familiar conviviente
        8. Familia de origen
        9. Relaciones familiares importantes
        10. Situación laboral o académica
        11. Eventos traumáticos o situaciones de riesgo
        12. Observaciones relevantes del profesional

        FORMATO DE RESPUESTA:
        - Usa títulos para cada sección.
        - Usa párrafos breves y fáciles de leer.
        - No agregues explicaciones externas.
        - No repitas información innecesariamente.

        El texto está en español.

        Texto:
        {text}

        Resultado:
        """
        
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
        )        
        return response.text.strip()
    except Exception as e:
        print(f"Error in AI summarization: {str(e)}")
        return "No se pudo generar el resumen."

