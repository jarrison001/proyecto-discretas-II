"""Funciones para verificar conectividad y ciclos en grafos."""

from graph_structures import DirectedGraph, UndirectedGraph


def _is_connected(graph: UndirectedGraph) -> bool:
    if not graph.vertices:
        return False

    start = graph.vertices[0]
    visited = {start}
    pending = [start]

    while pending:
        vertex = pending.pop()
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                pending.append(neighbor)

    return len(visited) == len(graph.vertices)


def is_connected(graph: UndirectedGraph) -> bool:
    """Imprime y retorna si el grafo no dirigido es conexo."""
    result = _is_connected(graph)
    print(f"is_connected: {result}")
    return result


def _has_undirected_cycle(graph: UndirectedGraph) -> bool:
    visited: set[str] = set()

    def visit(vertex: str, parent: str | None) -> bool:
        visited.add(vertex)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                if visit(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True
        return False

    for vertex in graph.vertices:
        if vertex not in visited and visit(vertex, None):
            return True
    return False


def _has_directed_cycle(graph: DirectedGraph) -> bool:
    # 0 = no visitado, 1 = en la ruta actual, 2 = recorrido terminado.
    state: dict[str, int] = {vertex: 0 for vertex in graph.vertices}

    def visit(vertex: str) -> bool:
        state[vertex] = 1
        for neighbor in graph.neighbors(vertex):
            if state[neighbor] == 1:
                return True
            if state[neighbor] == 0 and visit(neighbor):
                return True
        state[vertex] = 2
        return False

    return any(state[vertex] == 0 and visit(vertex) for vertex in graph.vertices)


def has_cycle(graph: UndirectedGraph | DirectedGraph) -> bool:
    """Imprime y retorna si el grafo contiene al menos un ciclo."""
    if isinstance(graph, UndirectedGraph):
        result = _has_undirected_cycle(graph)
    elif isinstance(graph, DirectedGraph):
        result = _has_directed_cycle(graph)
    else:
        raise TypeError("graph must be an UndirectedGraph or DirectedGraph")

    print(f"has_cycle: {result}")
    return result
