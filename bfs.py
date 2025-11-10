# implemente uma busca em largura em cima de uma das implementações de grafos que voce desejar

from dataclasses import dataclass, field

@dataclass
class Grafo:
    g: set = field(default_factory=set) 
    adjacency_list: dict[str, list[str]] = field(default_factory=dict)
    num_vertex: int = 0

    def bfs(self, starting_vertex : str):
        """
        1. Inserir o vértice inicial na fila
        2. Iniciar a lista de visitados vazia
        3. Enquanto a fila não estiver vazia:
            a. Retirar o primeiro vertice da fila
            b. Marcar vértice como visitado
            c. Obter os vizinhos do vértice
            d. Para cada vizinho:
                  i. Verificar se o vizinho já não está na fila
                 ii. Verificar se o vizinho já não foi visitado
                iii. Adicionar o vizinho na Fila
        4. Retornar visitados
        """
        queue = [starting_vertex] # vertice inicial
        visited = []

        while queue != []:
            pick = queue.pop()
            visited.append(pick)
            neighbours = self._get_neighbours(pick)

            for x in neighbours:
                if x in visited:
                    continue
                queue.append(x)
        
        return visited


    def _get_neighbours(self, vertex: str) -> list[str]:
        return self.adjacency_list[vertex]
    
    def add_vertex(self, vertex : str) -> bool:
        if vertex in self.adjacency_list.keys():
            return False
        
        self.adjacency_list[vertex] = []
        self.num_vertex += 1
    
    def add_path(self, v_from, v_to):
        self.adjacency_list[v_from].append(v_to)


g = Grafo()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")

g.add_path("A", "C")

print(g.bfs("A"))
