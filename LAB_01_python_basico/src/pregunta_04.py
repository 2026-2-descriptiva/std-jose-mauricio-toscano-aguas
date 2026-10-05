def pregunta_04():
    """
    Cuente cuántos registros hay en cada mes, usando la fecha de la tercera
    columna (`date`). Represente el mes como un texto de dos dígitos y retorne
    una lista de tuplas `(mes, cantidad)` ordenada por el mes.

    Ejemplo del formato de la respuesta:

        [("01", 3), ("02", 4), ("03", 2), ...]
    """


    import gzip
    counts = {}
    with gzip.open('data/data.csv.gz', 'rt') as f:
        for row in f:
            month = row.split('\t')[2].split('-')[1]
            counts[month] = counts.get(month, 0) + 1
    return sorted(counts.items())
