import os
from google import genai

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

client = genai.Client(
        vertexai=True,
        project="psicopanel-495600",
        location="us-west1",
    )
def correct_text(text: str):

    if not text:
        return ""

    try:
        prompt = f"""
                    Revisa, limpia y corrige el siguiente texto extraído mediante OCR.

                    INSTRUCCIONES:
                    - Corrige errores tipográficos, palabras mal reconocidas y problemas de puntuación.
                    - Mejora la coherencia y legibilidad del texto.
                    - Mantén el significado original y no inventes información.
                    - Conserva términos médicos, psicológicos o técnicos relevantes.
                    - Reestructura frases confusas únicamente cuando sea necesario para mejorar la comprensión.
                    - Elimina caracteres extraños, saltos de línea innecesarios y fragmentos repetidos producidos por el OCR.
                    - Separa el contenido en párrafos claros y ordenados.
                    - Respeta el idioma original del texto (español).

                    IMPORTANTE:
                    - No agregues nada al inicio del texto, solo devuelve el texto limpio
                    - No resumas el contenido.
                    - No agregues interpretaciones ni conclusiones.
                    - No omitas información relevante aunque parezca redundante.

                    Texto:
                    {text}

                    Texto corregido:
                  """

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
        )

        return response.text.strip()

    except Exception as e:
        print(f"Error in AI correction: {str(e)}")
        return text
