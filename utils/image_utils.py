import cv2

def preprocess_image(image):
    # Ejemplo: Redimensionar y normalizar
    image = cv2.resize(image, (640, 480))
    return image / 255.0