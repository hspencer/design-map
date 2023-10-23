import pandas as pd
import json

# Cargue los archivos CSV en DataFrames
nodes_df = pd.read_csv('nodes.csv')
relationship_df = pd.read_csv('relationship.csv')

# Convierta el DataFrame de 'nodes' de nuevo a una lista de diccionarios
nodes_list = nodes_df.rename(columns={'Materia': 'id', 'Tamaño': 'group'}).to_dict(orient='records')

# Convierta el DataFrame de 'relationship' de nuevo a una lista de diccionarios
links_list = []
for i, row in relationship_df.iterrows():
    source = row[0]
    for target, value in row[1:].items():
        if not pd.isna(value):
            links_list.append({
                'source': source,
                'target': target,
                'value': value
            })

# Combine 'nodes' y 'links' en un único objeto JSON
design_map = {
    'nodes': nodes_list,
    'links': links_list
}

# Guarde el objeto JSON en un archivo
with open('reconstructed_design_map.json', 'w', encoding='utf-8') as f:
    json.dump(design_map, f, ensure_ascii=False, indent=4)

print("Los archivos CSV se han convertido con éxito de nuevo a un único archivo JSON.")
