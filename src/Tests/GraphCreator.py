from numpy import random as r

from src.DiGraph import DiGraph


class GraphCreator:
    def __init__(self, seed: int, nodes: int, edges: int):
        self._seed = seed
        self._nodes = nodes
        self._edges = edges
        self._nodes_to_test = []
        self._graph = DiGraph()

    def create_graph(self) -> DiGraph:
        i = 0
        r.seed(self._seed)
        for i in range(self._nodes):
            x = r.uniform(35.0, 35.9)
            y = r.uniform(32.0, 32.9)
            z = 0
            self._graph.add_node(i, (x, y, z))
        i = 0
        while i < self._edges:
            x = r.randint(0, self._nodes)
            y = r.randint(0, self._nodes)
            w = r.uniform(0, 3)
            if self._graph.add_edge(x, y, w):
                i = i + 1
        return self._graph
