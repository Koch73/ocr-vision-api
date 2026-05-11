import cv2


def preprocess_image(image_path):
    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Mejorar contraste
    gray = cv2.equalizeHist(gray)

    # Binarización adaptativa
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    # Reducción de ruido
    denoise = cv2.medianBlur(thresh, 3)

    return denoise
