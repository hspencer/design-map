# Importar las bibliotecas necesarias para la manipulación de datos y la generación de JSON
import pandas as pd
import json

# 1. Importar el archivo CSV
csv_file_path = 'design-map.csv'  # Reemplace con la ruta al archivo CSV
df = pd.read_csv(csv_file_path)

# 2. Eliminar espacios en blanco al final de cada fila
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# 3. Importar nodos y sus relaciones
# Inicializar listas vacías para nodos y enlaces
nodes = []
links = []

# Poblar la lista 'nodes' y un diccionario temporal para contar enlaces
link_count_dict = {}

for index, row in df.iterrows():
    node_id = row[0]
    nodes.append({"id": node_id})
    link_count_dict[node_id] = 0  # Inicializar el conteo de enlaces para este nodo

    # Poblar la lista 'links'
    for linked_node in row[1:].dropna():
        links.append({"source": node_id, "target": linked_node})
        # Actualizar el conteo de enlaces para el nodo objetivo
        link_count_dict[linked_node] = link_count_dict.get(linked_node, 0) + 1

# 4. Calcular los tamaños de los nodos según la cantidad de veces que se enlazan
for node in nodes:
    node_id = node["id"]
    node["size"] = link_count_dict.get(node_id, 0)

# 5. Generar un objeto JSON para el grafo
graph_json = {"nodes": nodes, "links": links}
graph_json_str = json.dumps(graph_json, indent=4)

# Guardar el JSON en un archivo
with open('design-map-02.json', 'w') as f:
    json.dump(graph_json, f, indent=4)