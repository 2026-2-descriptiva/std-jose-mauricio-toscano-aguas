def pregunta_05():
    """
    Para cada letra de la primera columna (`letter`), encuentre el valor
    máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
    de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 9, 2), ("B", 9, 1), ...]
    """


    import gzip
    res = {}
    with gzip.open('data/data.csv.gz', 'rt') as f:
        for row in f:
            parts = row.split('\t')
            letter, val = parts[0], int(parts[1])
            if letter not in res:
                res[letter] = [val, val]
            else:
                res[letter][0] = max(res[letter][0], val)
                res[letter][1] = min(res[letter][1], val)
    return [(k, v[0], v[1]) for k, v in sorted(res.items())]
