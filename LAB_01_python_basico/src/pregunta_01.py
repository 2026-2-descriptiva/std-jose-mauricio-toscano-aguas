def pregunta_01():
    """
    Calcule la suma de los valores de la segunda columna (`value`) del
    archivo `data/data.csv.gz` y retorne el resultado como un número entero.

    Ejemplo del formato de la respuesta:

        214
    """


    import gzip
    with gzip.open('data/data.csv.gz', 'rt') as f:
        return sum(int(row.split('\t')[1]) for row in f)
