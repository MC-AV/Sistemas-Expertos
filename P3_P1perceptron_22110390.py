# PRACTICA 1 PARCIAL 3 22110390
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

# Aplicar la función signo
signo_resultados = np.sign(resultados)

# Mostrar los resultados de la función signo

# Calcular el término de corrección según la ecuación w0 + 1/2(y - y')x
# y' es el resultado de la función signo

# Inicializar el vector de pesos corregido (debe ser float64)
w_corregido = w.copy()

# Para cada ejemplo, aplicar la corrección
for i in range(len(y)):
    # Calcular el término de corrección: (y - y') * x
    correccion = (y[i] - signo_resultados[i]) * x[i] / 2
    w_corregido += correccion  # Actualizar los pesos
    testeo = np.dot(x, w_corregido)
    test_1 = np.sign(testeo)
    if np.all(test_1 == y): 
        a="Es correcto"
    else: 
        a = "Es incorrecto"

# Calcular el producto punto (w^T * x) para cada fila de x
# Mostrar los pesos corregidos
print(f" La W definitiva es:\n {w_corregido}\n")
print(f"La tabla de evalacion es:\n {x} \n")
print(f"Este es el resultado del test: {test_1} y esta es la Y original {y} \n")
print(f"El test es {a}\n")