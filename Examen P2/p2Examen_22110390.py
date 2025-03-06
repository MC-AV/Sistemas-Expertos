import cv2
import numpy as np
import matplotlib.pyplot as plt 

# Crear el kernel Laplaciano
kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])

# Leer la imagen en escala de grises
imagen = cv2.imread('P3.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar el filtro usando el kernel
imagen_filtrada = cv2.filter2D(imagen, -1, kernel)

# Mostrar la imagen original y la imagen filtrada
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(imagen, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Imagen con Kernel Laplaciano")
plt.imshow(imagen_filtrada, cmap='gray')
plt.axis('off')

plt.show()