"""Carga grafos desde archivos CSV con columnas source,target,weight."""

import csv
from pathlib import Path

from graph_structures import DirectedGraph, UndirectedGraph


REQUIRED_COLUMNS = {"source", "target", "weight"}


def _read_edges(file_path: str | Path) -> list[tuple[str, str, float]]:
    edges: list[tuple[str, str, float]] = []

    with Path(file_path).open("r", newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        columns = set(reader.fieldnames or [])
        missing_columns = REQUIRED_COLUMNS - columns
        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            raise ValueError(f"Missing required CSV columns: {missing}")

        for line_number, row in enumerate(reader, start=2):
            source = (row.get("source") or "").strip()
            target = (row.get("target") or "").strip()
            raw_weight = (row.get("weight") or "").strip()
            if not source or not target or not raw_weight:
                raise ValueError(f"Incomplete edge data on CSV line {line_number}")
            try:
                weight = float(raw_weight)
            except ValueError as error:
                raise ValueError(
                    f"Invalid weight on CSV line {line_number}: {raw_weight}"
                ) from error
            edges.append((source, target, weight))

    return edges


def load_undirected_graph(file_path: str | Path) -> UndirectedGraph:
    """Lee un CSV y crea un grafo no dirigido ponderado."""
    graph = UndirectedGraph()
    for source, target, weight in _read_edges(file_path):
        graph.add_edge(source, target, weight)
    return graph


def load_directed_graph(file_path: str | Path) -> DirectedGraph:
    """Lee un CSV y crea un grafo dirigido ponderado."""
    graph = DirectedGraph()
    for source, target, weight in _read_edges(file_path):
        graph.add_edge(source, target, weight)
    return graph
