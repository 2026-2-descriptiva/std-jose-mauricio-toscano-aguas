import os

def write_file(filename, body):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("    raise NotImplementedError", body)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

l3 = """
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
                data.append(current)
            parts = re.split(r'\s+', line.strip(), maxsplit=3)
            current = [int(parts[0]), int(parts[1]), float(parts[2].replace(',','.')), parts[3].strip()]
        elif line.strip():
            if current:
                current[3] += ' ' + line.strip()
    if current:
        current[3] = ' '.join(current[3].split())
        data.append(current)
    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    return df"""

l4 = """
    import os
    import pandas as pd
    for split in ['train', 'test']:
        data = []
        for target in ['negative', 'neutral', 'positive']:
            target_dir = os.path.join('data', split, target)
            for file in sorted(os.listdir(target_dir)):
                with open(os.path.join(target_dir, file), 'r', encoding='utf-8') as f:
                    data.append([f.read().strip(), target])
        df = pd.DataFrame(data, columns=['phrase', 'target'])
        os.makedirs('submission', exist_ok=True)
        df.to_csv(f'submission/{split}_dataset.csv', index=False)"""

l5 = """
    import pandas as pd
    import json
    import re
    import os
    
    df = pd.read_csv('data/ventas.csv.gz', sep=',', dtype=str, keep_default_na=False)
    
    # normalize columns
    cols = list(df.columns)
    for i in range(len(cols)):
        c = cols[i]
        c = c.replace('\\ufeff', '')
        c = c.strip().lower()
        c = re.sub(r'\\s+', '_', c)
        cols[i] = c
    df.columns = cols
    
    req_cols = ['supplier_id', 'supplier', 'country', 'city', 'purchase_date', 'amount', 'discount', 'weight', 'units', 'unit_price', 'contact_email']
    missing_required_columns = sorted(list(set(req_cols) - set(df.columns)))
    unexpected_columns = sorted(list(set(df.columns) - set(req_cols)))
    
    duplicate_row_count = int(df.duplicated(keep='first').sum())
    
    supp_counts = df['supplier_id'].value_counts()
    dupes_supps = supp_counts[supp_counts > 1].index
    duplicate_supplier_id_row_count = int(df['supplier_id'].isin(dupes_supps).sum())
    
    missing_value_count_by_column = {}
    for c in df.columns:
        cnt = df[c].apply(lambda x: 1 if x.strip() == '' or x.strip() == 'N/A' else 0).sum()
        missing_value_count_by_column[c] = int(cnt)
    
    def is_invalid_email(x):
        return not bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', x))
    
    invalid_email_count = int(df['contact_email'].apply(is_invalid_email).sum())
    
    def is_invalid_unit(x):
        if x.strip() == '' or x.strip() == 'N/A':
            return False
        try:
            val = float(x)
            return not (val.is_integer() and val > 0)
        except ValueError:
            return True
            
    invalid_unit_count = int(df['units'].apply(is_invalid_unit).sum())
    
    country_values = sorted(df['country'].unique().tolist())
    
    report = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "missing_required_columns": missing_required_columns,
        "unexpected_columns": unexpected_columns,
        "duplicate_row_count": duplicate_row_count,
        "duplicate_supplier_id_row_count": duplicate_supplier_id_row_count,
        "missing_value_count_by_column": missing_value_count_by_column,
        "invalid_email_count": invalid_email_count,
        "invalid_unit_count": invalid_unit_count,
        "country_values": country_values
    }
    
    os.makedirs('submission', exist_ok=True)
    with open('submission/data_quality_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    return report"""

write_file("LAB_03_ingestion_de_texto_plano/src/pregunta_01.py", l3)
write_file("LAB_04_ingestion_de_texto_en_directorios/src/pregunta_01.py", l4)
write_file("LAB_05_validacion_de_datos/src/pregunta_01.py", l5)
