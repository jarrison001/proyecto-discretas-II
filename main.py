"""Interfaz de línea de comandos para analizar un archivo de grafos."""

import argparse
from pathlib import Path

from csv_loader import load_directed_graph, load_undirected_graph
from graph_checks import has_cycle, is_connected
from graph_properties import is_forest, is_tree


def main() -> None:
    parser = argparse.ArgumentParser(description="Carga y analiza un grafo CSV.")
    parser.add_argument("file", type=Path, help="Ruta al CSV source,target,weight")
    parser.add_argument(
        "--type",
        choices=("undirected", "directed"),
        default="undirected",
        help="Tipo de grafo que se debe construir (por defecto: undirected)",
    )
    arguments = parser.parse_args()

    if arguments.type == "directed":
        graph = load_directed_graph(arguments.file)
        has_cycle(graph)
        return

    graph = load_undirected_graph(arguments.file)
    is_connected(graph)
    has_cycle(graph)
    is_tree(graph)
    is_forest(graph)


if __name__ == "__main__":
    main()
