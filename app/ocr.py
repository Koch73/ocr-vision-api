from app.google_vision_ocr import detect_handwritten_ocr
from app.ai.ai_correction import correct_text


def extract_text(image_path):
    processed = detect_handwritten_ocr(image_path)
    
    # Correct text imperfections using AI
    if "text" in processed:
        processed["text"] = correct_text(processed["text"])
    return processed
