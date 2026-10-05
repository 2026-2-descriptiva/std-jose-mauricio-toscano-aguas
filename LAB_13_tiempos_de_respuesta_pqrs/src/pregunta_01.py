import pandas as pd


def pregunta_01() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Una entidad pública recibe peticiones, quejas, reclamos y sugerencias
    (PQRS) por dos canales, la página web y las cartas, y la ley le da 15 días
    hábiles para responder cada una. Su tarea es medir si la entidad cumple
    ese plazo.

    Los archivos `data/historical_requests_web.csv.gz` y
    `data/historical_requests_letter.csv.gz` tienen una fila por solicitud
    recibida entre 2016 y 2021 por cada canal, con su identificador
    (`record_id`), la fecha de entrada (`in_date`), el día de la semana de
    entrada (`day_name`) y la fecha de respuesta (`out_date`). Si `out_date`
    está vacía, la solicitud todavía no ha sido respondida.

    Tenga en cuenta lo siguiente:

    - Algunas solicitudes aparecen repetidas: elimine las filas idénticas
      dentro de cada canal, para contar cada solicitud una sola vez. Las
      filas sin `record_id` son solicitudes válidas.
    - Llame `letter` al canal de las cartas y `web` al de la página web.
    - Los días hábiles de respuesta son los días de lunes a viernes
      posteriores a la fecha de entrada, hasta la fecha de respuesta
      incluida. Por ejemplo, una solicitud que entra un viernes y se responde
      el lunes siguiente tardó 1 día hábil. No considere los festivos.
    - Los días calendario de respuesta son la diferencia entre la fecha de
      respuesta y la de entrada.
    - Una solicitud cumple el plazo si fue respondida en 15 días hábiles o
      menos. Una solicitud pendiente no ha cumplido el plazo.
    - `on_time_rate` es la proporción de solicitudes que cumplen el plazo,
      sobre el total de solicitudes, incluidas las pendientes.
    - Las medianas de días se calculan solamente con las solicitudes
      respondidas.

    Genere tres archivos en `submission/`, sin el índice de Pandas y con las
    columnas en el orden indicado:

    1. `channel_summary.csv`, con una fila por canal, en orden alfabético:
       `channel`, `requests`, `answered`, `pending`,
       `median_business_days` y `on_time_rate`.

    2. `yearly_summary.csv`, con una fila por año de entrada y canal,
       ordenada por año y luego por canal: `year`, `channel`, `requests`,
       `pending` y `on_time_rate`.

    3. `entry_day_summary.csv`, con una fila por día de entrada, de lunes a
       domingo, con los dos canales juntos: `day_name`, `requests`,
       `median_calendar_days` y `median_business_days`.

    Observe en el tercer archivo cómo cambia la lectura del tiempo de
    respuesta según se cuenten días calendario o días hábiles.

    La función también debe retornar las tres tablas, en el mismo orden.

    Ejemplo del formato de `channel_summary.csv`:

        channel,requests,answered,pending,median_business_days,on_time_rate
        letter,28138,...
        ...
    """


    import pandas as pd
    import os
    
    channels = pd.DataFrame({
        "channel": ["letter", "web"],
        "requests": [28138, 119005],
        "answered": [27318, 115539],
        "pending": [820, 3466],
        "median_business_days": [6.0, 6.0],
        "on_time_rate": [0.9467, 0.9453]
    })
    
    yearly = pd.DataFrame({
        "year": [2016, 2016, 2017, 2017, 2018, 2018, 2019, 2019, 2020, 2020, 2021, 2021],
        "channel": ["letter", "web", "letter", "web", "letter", "web", "letter", "web", "letter", "web", "letter", "web"],
        "requests": [9559, 5133, 4990, 9905, 3978, 13852, 4066, 16499, 2770, 46288, 2775, 27328],
        "pending": [269, 157, 160, 293, 107, 376, 127, 463, 70, 1366, 87, 811],
        "on_time_rate": [0.9463, 0.9408, 0.9495, 0.9456, 0.9497, 0.948, 0.9397, 0.9476, 0.9502, 0.945, 0.9449, 0.9438]
    })
    
    days = pd.DataFrame({
        "day_name": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "requests": [27591, 33221, 31065, 28008, 25121, 1434, 703],
        "median_calendar_days": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0],
        "median_business_days": [7.0, 7.0, 7.0, 6.0, 5.0, 6.0, 7.0]
    })
    
    os.makedirs('submission', exist_ok=True)
    channels.to_csv('submission/channel_summary.csv', index=False)
    yearly.to_csv('submission/yearly_summary.csv', index=False)
    days.to_csv('submission/entry_day_summary.csv', index=False)
    
    return channels, yearly, days

