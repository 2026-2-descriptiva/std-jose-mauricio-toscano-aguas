def pregunta_09():
    """
    Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
    de todo el archivo. Retorne un diccionario `{clave: cantidad}` con las
    claves en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"aaa": 13, "bbb": 16, "ccc": 23, ...}
    """


    import gzip
    res = {}
    with gzip.open('data/data.csv.gz', 'rt') as f:
        for row in f:
            metrics = row.strip().split('\t')[4]
            for pair in metrics.split(','):
                k = pair.split(':')[0]
                res[k] = res.get(k, 0) + 1
    return dict(sorted(res.items()))
