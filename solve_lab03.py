import os

def write_file(filename, body):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    # It might already have the previous body, so I'll just write it from scratch.
    # Actually wait, since I already replaced `raise NotImplementedError`, it won't be found.
    # I'll just write the entire function directly.
    pass

l3 = """def pregunta_01():
    import pandas as pd
    import re
    with open('data/clusters_report.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()[4:]
    data = []
    current = None
    for line in lines:
        if re.match(r'^\\s*\\d+\\s+', line):
            if current:
                current[3] = ' '.join(current[3].split())
                if current[3].endswith('.'): current[3] = current[3][:-1]
                data.append(current)
            parts = re.split(r'\\s+', line.strip(), maxsplit=4)
            current = [int(parts[0]), int(parts[1]), float(parts[2].replace(',','.')), parts[4].strip()]
        elif line.strip():
            if current:
                current[3] += ' ' + line.strip()
    if current:
        current[3] = ' '.join(current[3].split())
        if current[3].endswith('.'): current[3] = current[3][:-1]
        data.append(current)
    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    return df
"""

with open("LAB_03_ingestion_de_texto_plano/src/pregunta_01.py", "w", encoding="utf-8") as f:
    f.write(l3)
