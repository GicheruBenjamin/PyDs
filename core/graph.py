

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)  # undirected

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} → {self.adj_list[vertex]}")
