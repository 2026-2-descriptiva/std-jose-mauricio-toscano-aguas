def pregunta_06():
    """
    La quinta columna (`metrics`) contiene pares `clave:valor` separados por
    comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
    aparecen en todo el archivo. Retorne una lista de tuplas
    `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.

    Observe que el orden es mínimo y luego máximo, al contrario de la
    pregunta 5.

    Ejemplo del formato de la respuesta:

        [("aaa", 1, 9), ("bbb", 1, 9), ...]
    """


    import gzip
    res = {}
    with gzip.open('data/data.csv.gz', 'rt') as f:
        for row in f:
            metrics = row.strip().split('\t')[4]
            for pair in metrics.split(','):
                k, v = pair.split(':')
                v = int(v)
                if k not in res:
                    res[k] = [v, v]
                else:
                    res[k][0] = min(res[k][0], v)
                    res[k][1] = max(res[k][1], v)
    return [(k, v[0], v[1]) for k, v in sorted(res.items())]
