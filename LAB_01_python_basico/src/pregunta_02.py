def pregunta_02():
    """
    Cuente cuántos registros hay para cada letra de la primera columna
    (`letter`). Retorne una lista de tuplas `(letra, cantidad)` ordenada
    alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 8), ("B", 7), ("C", 5), ...]
    """


    import gzip
    counts = {}
    with gzip.open('data/data.csv.gz', 'rt') as f:
        for row in f:
            letter = row.split('\t')[0]
            counts[letter] = counts.get(letter, 0) + 1
    return sorted(counts.items())
