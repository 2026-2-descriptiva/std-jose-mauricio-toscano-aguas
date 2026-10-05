def pregunta_01():
    import pandas as pd
    import re
    with open('data/clusters_report.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()[4:]
    data = []
    current = None
    for line in lines:
        if re.match(r'^\s*\d+\s+', line):
            if current:
                current[3] = ' '.join(current[3].split())
                if current[3].endswith('.'): current[3] = current[3][:-1]
                data.append(current)
            parts = re.split(r'\s+', line.strip(), maxsplit=4)
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
