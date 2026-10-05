def pregunta_12():
    """
    Para cada letra de la primera columna (`letter`), sume todos los valores
    numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
    Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"A": 177, "B": 187, "C": 114, ...}
    """


    import gzip
    res = {}
    with gzip.open('data/data.csv.gz', 'rt') as f:
        for row in f:
            parts = row.strip().split('\t')
            letter = parts[0]
            val = sum(int(p.split(':')[1]) for p in parts[4].split(','))
            res[letter] = res.get(letter, 0) + val
    return dict(sorted(res.items()))
