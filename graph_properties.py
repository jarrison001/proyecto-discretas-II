"""Funciones para clasificar árboles y bosques no dirigidos."""

from graph_checks import _has_undirected_cycle, _is_connected
from graph_structures import UndirectedGraph


def is_tree(graph: UndirectedGraph) -> bool:
    """Imprime y retorna si el grafo no dirigido es un árbol."""
    result = bool(graph.vertices) and _is_connected(graph) and not _has_undirected_cycle(graph)
    print(f"is_tree: {result}")
    return result


def is_forest(graph: UndirectedGraph) -> bool:
    """Imprime y retorna si el grafo no dirigido es un bosque."""
    result = not _has_undirected_cycle(graph)
    print(f"is_forest: {result}")
    return result
