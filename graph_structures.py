"""Representaciones de grafos ponderados, dirigidos y no dirigidos."""


class UndirectedGraph:
    """Grafo no dirigido representado mediante listas de adyacencia."""

    def __init__(self) -> None:
        self.adjacency: dict[str, dict[str, float]] = {}

    @property
    def vertices(self) -> list[str]:
        return list(self.adjacency)

    def add_vertex(self, vertex: str) -> None:
        self.adjacency.setdefault(vertex, {})

    def add_edge(self, source: str, target: str, weight: float) -> None:
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency[source][target] = weight
        self.adjacency[target][source] = weight

    def neighbors(self, vertex: str) -> dict[str, float]:
        return self.adjacency[vertex]


class DirectedGraph:
    """Grafo dirigido representado mediante listas de adyacencia."""

    def __init__(self) -> None:
        self.adjacency: dict[str, dict[str, float]] = {}

    @property
    def vertices(self) -> list[str]:
        return list(self.adjacency)

    def add_vertex(self, vertex: str) -> None:
        self.adjacency.setdefault(vertex, {})

    def add_edge(self, source: str, target: str, weight: float) -> None:
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency[source][target] = weight

    def neighbors(self, vertex: str) -> dict[str, float]:
        return self.adjacency[vertex]
