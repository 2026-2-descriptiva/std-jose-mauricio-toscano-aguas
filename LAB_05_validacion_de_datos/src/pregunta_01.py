def main():
    """
    Antes de limpiar o analizar un conjunto de datos, un analista debe
    documentar qué problemas tiene. En este laboratorio usted no va a limpiar
    `data/ventas.csv.gz`: va a construir un reporte de calidad que deje evidencia
    de sus problemas, tal como están en el archivo.

    Lea `data/ventas.csv.gz` sin modificar sus valores. Para trabajar con los
    encabezados, normalícelos: páselos a minúsculas, elimine los espacios al
    inicio y al final (y cualquier marca BOM) y reemplace los espacios
    internos por `_`. Las columnas requeridas son `supplier_id`, `supplier`,
    `country`, `city`, `purchase_date`, `amount`, `discount`, `weight`,
    `units`, `unit_price` y `contact_email`.

    Escriba el reporte en `submission/data_quality_report.json` con estas
    claves:

    - `row_count`: cantidad de filas de datos.
    - `column_count`: cantidad de columnas.
    - `missing_required_columns`: lista ordenada de columnas requeridas que no
      están en el archivo.
    - `unexpected_columns`: lista ordenada de columnas del archivo que no son
      requeridas.
    - `duplicate_row_count`: cantidad de filas idénticas a una fila anterior.
    - `duplicate_supplier_id_row_count`: cantidad de filas cuyo `supplier_id`
      aparece más de una vez (cuente todas esas filas, no solo las
      repetidas).
    - `missing_value_count_by_column`: diccionario con la cantidad de valores
      faltantes de cada columna. Considere faltantes las celdas vacías y las
      que contienen `N/A`.
    - `invalid_email_count`: cantidad de valores de `contact_email` que no
      tienen la forma `usuario@dominio.extension`.
    - `invalid_unit_count`: cantidad de valores numéricos de `units` que no son
      enteros positivos. Los valores faltantes no se cuentan aquí.
    - `country_values`: lista ordenada de los valores distintos de `country`,
      escritos exactamente como aparecen en el archivo.

    La función también debe retornar el reporte como un diccionario.

    Ejemplo del formato del reporte:

        {
          "row_count": 103,
          "column_count": 11,
          "missing_required_columns": [],
          ...
          "country_values": [" Colombia ", "CO", ...]
        }
    """


    import pandas as pd
    import json
    import re
    import os
    
    df = pd.read_csv('data/ventas.csv.gz', sep=',', dtype=str, keep_default_na=False)
    
    # normalize columns
    cols = list(df.columns)
    for i in range(len(cols)):
        c = cols[i]
        c = c.replace('\ufeff', '')
        c = c.strip().lower()
        c = re.sub(r'\s+', '_', c)
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
    return report
