def pregunta_08():
    """
    Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
    letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
    tuplas `(valor, letras)` ordenada por el valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["B", "E"]), (2, ["A", "E"]), ...]
    """


    import gzip
    res = {}
    with gzip.open('data/data.csv.gz', 'rt') as f:
        for row in f:
            parts = row.split('\t')
            letter, val = parts[0], int(parts[1])
            res.setdefault(val, set()).add(letter)
    return sorted((k, sorted(list(v))) for k, v in res.items())
