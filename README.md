# Proyecto de grafos

Proyecto de Matemáticas Discretas II para representar grafos dirigidos y no dirigidos ponderados, leerlos desde CSV y analizar sus propiedades.

## Requisitos

- Python 3.10 o superior.
- [UV](https://docs.astral.sh/uv/).

No se usan librerías externas para implementar grafos. Las funciones están en inglés, como pide la guía.

## Preparar el entorno

Desde esta carpeta, ejecuta:

```powershell
uv sync
```

## Ejecutar el análisis

Para cargar y analizar un grafo no dirigido:

```powershell
uv run main.py ejemplos/ejemplo_1.csv
```

Para construir un grafo dirigido desde el mismo formato de archivo:

```powershell
uv run main.py ejemplos/ejemplo_1.csv --type directed
```

Los archivos deben tener encabezados `source,target,weight`. Los vértices se leen como texto y los pesos como números.

## Representaciones

Ambos tipos de grafo usan listas de adyacencia: cada vértice tiene un diccionario de vecinos y pesos. En el grafo no dirigido, cada arista se guarda en las dos direcciones. En el dirigido, se guarda únicamente desde el origen hacia el destino. Elegí esta representación porque permite consultar directamente los vecinos de un vértice y expresa las dos convenciones con claridad.

## Funciones

- `load_undirected_graph` y `load_directed_graph`: leen el CSV y construyen la representación correspondiente.
- `is_connected`: verifica conectividad en un grafo no dirigido.
- `has_cycle`: detecta ciclos en grafos dirigidos y no dirigidos.
- `is_tree`: verifica que el grafo no dirigido sea conexo y no tenga ciclos.
- `is_forest`: verifica que el grafo no dirigido no tenga ciclos; puede estar desconectado.

Las funciones de conectividad, ciclos, árbol y bosque imprimen el resultado en el formato `nombre_de_la_funcion: resultado` y también lo retornan.

## Ejemplos entregados

La carpeta `ejemplos/` contiene los seis CSV incluidos con la consigna. Presentan grafos conexos, desconectados, ciclos y un grafo completo; permiten observar cómo cambian las propiedades calculadas.

## Estructura del proyecto

```text
proyecto_grafos/
├── csv_loader.py
├── graph_checks.py
├── graph_properties.py
├── graph_structures.py
├── main.py
├── pyproject.toml
└── ejemplos/
```

## Experiencia y decisión de diseño

La lista de adyacencia mantiene juntas las conexiones de cada vértice y sus pesos. La diferencia entre grafo dirigido y no dirigido queda concentrada en la forma de agregar una arista. El proyecto se divide por responsabilidades: estructuras, lectura de archivos, verificaciones y ejecución.
