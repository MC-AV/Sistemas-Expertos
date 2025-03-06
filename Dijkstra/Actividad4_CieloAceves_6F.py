import pandas as pd

class Graph:
    def __init__(self, grafo):
        self.grafo = grafo  # DataFrame para representar el grafo
        self.vertices = list(grafo.columns)  # Lista de vértices

    def dijkstra(self, start, end):
        # Inicializar las etiquetas de distancia y el conjunto de vértices no procesados
        L = {vertex: float('inf') for vertex in self.vertices}  # Distancia infinita inicialmente
        L[start] = 0  # Distancia desde el vértice inicial a sí mismo es 0
        T = set(self.vertices)  # Conjunto de vértices no procesados

        while end in T:
            # Seleccionar el vértice con la distancia mínima
            u = min(T, key=lambda vertex: L[vertex])

            # Si la distancia mínima es infinita, no hay más vértices alcanzables
            if L[u] == float('inf'):
                break

            T.remove(u)

            # Actualizar las etiquetas de distancia de los vértices adyacentes
            for neighbor in self.vertices:
                if self.grafo.at[u, neighbor] > 0:  # Verificar si existe una arista
                    new_distance = L[u] + self.grafo.at[u, neighbor]
                    if new_distance < L[neighbor]:
                        L[neighbor] = new_distance

        return L[end]

# Leer la gráfica desde un archivo de Excel
grafo = pd.read_excel('Datos_.xlsx', sheet_name='Sheet1', index_col=0)

# Crear un objeto Graph con el DataFrame leído
g = Graph(grafo)

# Solicitar al usuario que ingrese los nodos de inicio y fin
nodo_inicial = input("Ingrese el nodo inicial: ")
nodo_final = input("Ingrese el nodo final: ")

# Validar si los nodos ingresados existen en el grafo
if nodo_inicial in g.vertices and nodo_final in g.vertices:
    # Encontrar la longitud de la ruta más corta usando el algoritmo de Dijkstra
    shortest_path_length = g.dijkstra(nodo_inicial, nodo_final)
    
    if shortest_path_length == float('inf'):
        print(f"No hay una ruta disponible de {nodo_inicial} a {nodo_final}.")
    else:
        print(f"La longitud de la ruta más corta de {nodo_inicial} a {nodo_final} es {shortest_path_length}")
else:
    print("Uno o ambos de los nodos ingresados no existen en el grafo. Por favor, intente nuevamente con nodos válidos.")
