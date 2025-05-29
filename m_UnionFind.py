# Esta clase nos ayudará a detectar ciclos de manera eficiente.
class UnionFind:
    def __init__(self, nodes):
        # 'parent' almacena el padre de cada elemento. Inicialmente, cada elemento es su propio padre.
        self.parent = {node: node for node in nodes}
        # 'rank' (o altura/tamaño) se usa para optimizar la operación de unión, manteniendo los árboles planos.
        self.rank = {node: 0 for node in nodes}

    def find(self, i):
        # Encuentra el representante (raíz) del conjunto al que pertenece 'i'.
        # Realiza 'path compression' para aplanar el árbol y acelerar futuras búsquedas.
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # Une los conjuntos que contienen a 'i' y 'j'.
        # Retorna True si se realizó una unión (es decir, i y j estaban en conjuntos diferentes),
        # y False si ya estaban en el mismo conjunto (indicando un ciclo).
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Unión por rango para mantener el árbol más plano (optimización).
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_j] < self.rank[root_i]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True # Se unieron dos conjuntos diferentes
        return False # Ya estaban en el mismo conjunto, añadir esta arista formaría un ciclo