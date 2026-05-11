from google.cloud import vision_v1p3beta1 as vision
# from google.oauth2 import service_account


def detect_handwritten_ocr(path):
    """Detects handwritten characters in a local image.

    Args:
    path: The path to the local file.
    """
    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # Language hint codes for handwritten OCR:
    # Note: Use only one language hint code per request for handwritten OCR.
    image_context = vision.ImageContext(language_hints=["es-t-i0-handwrit"])

    response = client.document_text_detection(
        image=image, image_context=image_context)

    full_txt = response.full_text_annotation.text

    for page in response.full_text_annotation.pages:
        c_blk = acum_blk_confidence = 0
        for block in page.blocks:
            c_blk += 1
            acum_blk_confidence += block.confidence

    # make the statistics
    if c_blk != 0:
        avg_confidence = acum_blk_confidence / c_blk

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(
                response.error.message)
        )
    data = {"text": full_txt, "avg_confidence": avg_confidence}

    return data
