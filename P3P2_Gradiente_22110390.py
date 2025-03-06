# PRACTICA 2 PARCIAL 3 22110390
import numpy as np

# Definir la matriz X (de tamaño 4x3)
x = np.array([
    [ 1, -1, -1], 
    [ 1, -1,  1], 
    [ 1,  1, -1], 
    [ 1,  1,  1]
])

# Definir el vector de pesos w (de tamaño 3) como tipo float64
w = np.array([1, 1, 1], dtype=np.float64)

# Vector de etiquetas reales y (en este caso, valores arbitrarios, pueden ser +1 o -1)
y = np.array([-1, -1, -1, 1])

# Calcular el producto punto (w^T * x) para cada fila de x
resultados = np.dot(x, w)

# Calcular el gradiente para una función de pérdida L(w) = -y * (x · w)
# Gradiente: ∇L(w) = -∑(y * x), para los errores
gradiente = np.zeros_like(w, dtype=np.float64)

for i in range(len(y)):
    if y[i] * resultados[i] <= 0:  # Considerar solo ejemplos mal clasificados
        gradiente += -y[i] * x[i]  # Gradiente acumulado

# Mostrar los resultados
print("Gradiente calculado:")
print(gradiente)

# Actualizar los pesos usando el gradiente descendente
learning_rate = 0.1
w_actualizado = w - learning_rate * gradiente

# Mostrar los pesos actualizados
print("\nPesos actualizados:")
print(w_actualizado)
