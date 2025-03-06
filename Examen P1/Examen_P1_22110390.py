import pandas as pd

class Graph:
    def __init__(self, grafo):
        self.grafo = grafo  # DataFrame para representar el grafo
        self.vertices = list(grafo.columns)  # Extra los datos y lo guarda Lista de vértices

    def prim(self, start):
        # Inicializar variables
        n = len(self.vertices)
        selected = {vertex: False for vertex in self.vertices}  # v(i) = 1 si el vértice está en el AEM
        selected[start] = True  # Empezar desde el vértice inicial
        edges = []  # Lista para almacenar las aristas del árbol de expansión mínima
        total_weight = 0  # Peso total del árbol de expansión mínima

        for _ in range(n - 1):
            min_edge = None# almacenar el vertice de menor peso
            min_weight = float('inf')

            # Buscar la arista de peso mínimo con un vértice en el AEM y otro que no esté en el AEM
            for u in self.vertices:
                if selected[u]:
                    for v in self.vertices:
                        if not selected[v] and 0 < self.grafo.at[u, v] < min_weight:
                            min_weight = self.grafo.at[u, v]
                            min_edge = (u, v)

            if min_edge:
                u, v = min_edge
                edges.append((u, v, min_weight))  # Agregar la arista al AEM
                total_weight += min_weight
                selected[v] = True  # Marcar el vértice como agregado al AEM

        return edges, total_weight

# Leer la gráfica desde un archivo de Excel
grafo = pd.read_excel('Datos.xlsx', sheet_name='Sheet1', index_col=0)

# Crear un objeto Graph con el DataFrame leído
g = Graph(grafo)

# Solicitar al usuario que ingrese el nodo inicial
nodo_inicial = input("Ingrese el nodo inicial: ")

# Validar si el nodo ingresado existe en el grafo
if nodo_inicial in g.vertices:
    # Encontrar el árbol de expansión mínima usando el algoritmo de Prim.
    #  mst_edges lista de aristas
    mst_edges, mst_weight = g.prim(nodo_inicial)

    if mst_edges:
        print(f"El árbol de expansión mínima tiene un peso total de {mst_weight}.")
        print("Las aristas del árbol de expansión mínima son:")
        for edge in mst_edges:
            print(f"{edge[0]} - {edge[1]} con peso {edge[2]}")
    else:
        print(f"No se pudo encontrar un árbol de expansión mínima desde el nodo {nodo_inicial}.")
else:
    print("El nodo ingresado no existe en el grafo. Por favor, intente nuevamente con un nodo válido.")
