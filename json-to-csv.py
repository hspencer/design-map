import pandas as pd
import json

# Cargue sus datos JSON en la variable design_map
with open('design-map.json', 'r', encoding='utf-8') as f:
    design_map = json.load(f)

# Extraiga los nodos y los enlaces de los datos JSON
nodes = design_map['nodes']
links = design_map['links']

# Convierta los nodos en un DataFrame
nodes_df = pd.DataFrame(nodes)
nodes_df = nodes_df.rename(columns={'id': 'Materia', 'group': 'Tamaño'})

# Inicialice un DataFrame NxN para las relaciones
relationship_df = pd.DataFrame(index=[node['id'] for node in nodes], columns=[node['id'] for node in nodes])

# Rellene el DataFrame de relaciones en función de los enlaces
for link in links:
    source = link['source']
    target = link['target']
    value = link.get('value', 1)  # Use 1 as the default value if 'value' is not present
    relationship_df.at[source, target] = value
    relationship_df.at[target, source] = value

# Guarde los DataFrames como archivos CSV
nodes_df.to_csv('nodes.csv', index=False, encoding='utf-8')
relationship_df.to_csv('relationship.csv', encoding='utf-8')
