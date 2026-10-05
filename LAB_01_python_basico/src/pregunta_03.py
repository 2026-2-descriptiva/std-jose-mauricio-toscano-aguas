def pregunta_03():
    """
    Sume los valores de la segunda columna (`value`) para cada letra de la
    primera columna (`letter`). Retorne una lista de tuplas `(letra, suma)`
    ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 53), ("B", 36), ("C", 27), ...]
    """


    import gzip
    sums = {}
    with gzip.open('data/data.csv.gz', 'rt') as f:
        for row in f:
            parts = row.split('\t')
            sums[parts[0]] = sums.get(parts[0], 0) + int(parts[1])
    return sorted(sums.items())
