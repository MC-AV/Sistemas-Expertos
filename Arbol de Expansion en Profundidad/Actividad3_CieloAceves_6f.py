import pandas as pd

class Graph:
    def __init__(self, grafo):
        self.grafo = grafo  # DataFrame para representar el grafo
        self.vertices = list(grafo.columns)  # Lista de vértices

    def dfs_tree(self, v, visited, parent, tree_edges, tree_vertices):
        """
        Algoritmo de búsqueda en profundidad para encontrar el árbol de expansión.
        """
        visited[v] = True  # Marcar el vértice actual como visitado
        tree_vertices.add(v)  # Agregar el vértice al conjunto de V'

        for neighbour in sorted(self.vertices):
            if self.grafo.at[v, neighbour] > 0:  # Verificar si existe una arista
                if not visited[neighbour]:
                    tree_edges.append((v, neighbour))  # Añadir la arista al árbol de expansión
                    parent[neighbour] = v  # Establecer el vértice padre
                    self.dfs_tree(neighbour, visited, parent, tree_edges, tree_vertices)
                elif neighbour != parent[v]:
                    # Si el vecino ya fue visitado y no es el padre, omitir para evitar ciclo
                    continue

    def find_spanning_tree(self, start_vertex):
        """
        Encuentra el árbol de expansión a partir del vértice de inicio dado.
        """
        visited = {vertex: False for vertex in self.vertices}
        parent = {vertex: None for vertex in self.vertices}
        tree_edges = []
        tree_vertices = set()  # Conjunto de vértices del árbol de expansión V'

        self.dfs_tree(start_vertex, visited, parent, tree_edges, tree_vertices)

        return tree_vertices, tree_edges


# Leer la gráfica desde un archivo de Excel
grafo = pd.read_excel('Datos.xlsx', sheet_name='Sheet1', index_col=0)

# Crear un objeto Graph con el DataFrame leído
g = Graph(grafo)

# Solicitar al usuario que ingrese el nodo inicial
nodo_inicial = input("Ingrese el nodo inicial para comenzar la búsqueda: ")

# Validar si el nodo inicial existe en el grafo
if nodo_inicial in grafo.columns:
    # Encontrar el árbol de expansión a partir del nodo inicial
    tree_vertices, spanning_tree = g.find_spanning_tree(nodo_inicial)
    
    # Imprimir los vértices y las aristas del árbol de expansión
    print("Vértices del árbol de expansión V':", tree_vertices)
    print("Árbol de expansión encontrado desde el nodo", nodo_inicial, ":", spanning_tree)
else:
    print("El nodo ingresado no existe en el grafo. Por favor, intente nuevamente con un nodo válido.")
