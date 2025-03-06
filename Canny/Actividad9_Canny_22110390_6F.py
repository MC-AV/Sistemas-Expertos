import cv2
import numpy as np

# Inicializa la captura de video desde la cámara
screen = cv2.VideoCapture(0)

if not screen.isOpened():
    print("Error al abrir la cámara.")
    exit()

while True:
    # Captura cada frame de la cámara
    ret, frame = screen.read()
    
    if not ret:
        print("No se pudo obtener el frame.")
        break

    # Convierte la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplica el algoritmo de detección de bordes Canny
    edges = cv2.Canny(gray, 100, 200)

    # Muestra el frame original y el resultado de Canny
    cv2.imshow('Frame Original', frame)
    cv2.imshow('Bordes Canny', edges)

    # Para salir presione 'e'
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

# Libera los recursos y cierra las ventanas
screen.release()
cv2.destroyAllWindows()
