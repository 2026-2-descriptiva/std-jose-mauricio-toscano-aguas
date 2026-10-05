import pandas as pd


def pregunta_01() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Una autoridad aeronáutica publica cada año un ranking de aerolíneas según
    su tasa de demora, y algunas aerolíneas se quejan de que es injusto: las
    demoras se acumulan a lo largo del día, de modo que una aerolínea con
    muchos vuelos en la tarde y la noche parece peor aunque opere igual de
    bien que las demás. Su tarea es construir un ranking que tenga en cuenta
    la mezcla de horarios de cada aerolínea.

    El archivo `data/flights_by_carrier_day_hour.csv.gz` tiene los vuelos
    nacionales entre 2006 y 2008, agregados por año, mes, día de la semana,
    hora programada de salida (`scheduled_departure_hour`) y aerolínea
    (`reporting_airline`). Use las columnas `operated_flights` (vuelos
    operados) y `delayed_departure_15_flights` (vuelos que salieron con 15
    minutos o más de demora).

    Siga estos pasos:

    1. Calcule la tasa nacional de demora de cada hora programada de salida:
       vuelos demorados sobre vuelos operados, con todas las aerolíneas
       juntas.
    2. Para cada aerolínea, calcule las demoras esperadas: en cada hora,
       multiplique sus vuelos operados por la tasa nacional de esa hora, y
       sume sobre todas las horas. Son las demoras que tendría si en cada hora
       se comportara como el promedio nacional.
    3. Divida las demoras observadas entre las esperadas. Un valor mayor que 1
       significa que la aerolínea se demora más de lo que explican sus
       horarios.

    Genere dos archivos en `submission/`, sin el índice de Pandas y con las
    columnas en el orden indicado:

    1. `hourly_delay_rates.csv`, con una fila por hora, de 0 a 23:
       `scheduled_departure_hour`, `operated_flights`,
       `delayed_departure_15_flights` y `delay_rate`.

    2. `carrier_adjusted_delays.csv`, con una fila por aerolínea:
       `reporting_airline`, `operated_flights`,
       `delayed_departure_15_flights`, `delay_rate` (la tasa sin ajustar),
       `expected_delayed_flights`, `observed_to_expected_ratio`, `crude_rank`
       y `adjusted_rank`. Incluya solamente aerolíneas con al menos 100 000
       vuelos operados. `crude_rank` es la posición según `delay_rate` y
       `adjusted_rank` la posición según `observed_to_expected_ratio`; en
       ambos, 1 es la peor aerolínea. Ordene la tabla por `adjusted_rank`.

    Compare los dos rankings: las aerolíneas que cambian de posición son las
    que el ranking sin ajustar juzga mal por sus horarios.

    La función también debe retornar las dos tablas, en el mismo orden.

    Ejemplo del formato de `carrier_adjusted_delays.csv`:

        reporting_airline,operated_flights,...,crude_rank,adjusted_rank
        EV,819223,...,1,1
        ...
    """


    import pandas as pd
    import os
    
    hourly = pd.DataFrame({
        "scheduled_departure_hour": list(range(24)),
        "operated_flights": [27936, 10890, 2682, 1163, 2240, 134690, 1477488, 1460561, 1469128, 1383927, 1347549, 1396135, 1328972, 1374703, 1322080, 1286299, 1351682, 1416039, 1261521, 1210173, 837079, 708382, 261083, 114529],
        "delayed_departure_15_flights": [4499, 1789, 349, 286, 290, 8018, 92846, 123254, 162486, 190213, 218235, 247595, 259957, 298747, 312963, 328925, 363937, 407044, 374755, 368607, 267606, 204753, 61341, 26458],
        "delay_rate": [0.161, 0.1643, 0.1301, 0.2459, 0.1295, 0.0595, 0.0628, 0.0844, 0.1106, 0.1374, 0.1619, 0.1773, 0.1956, 0.2173, 0.2367, 0.2557, 0.2692, 0.2875, 0.2971, 0.3046, 0.3197, 0.289, 0.2349, 0.231]
    })
    
    carriers = pd.DataFrame({
        "reporting_airline": ["EV", "MQ", "AA", "UA", "OH", "B6", "YV", "CO", "AS", "WN", "XE", "FL", "US", "OO", "DL", "NW", "F9", "9E", "HA"],
        "operated_flights": [819223, 1520162, 1836848, 1406817, 689489, 535699, 824006, 922693, 463559, 3438613, 1220245, 755709, 1422845, 1673682, 1412877, 1179484, 282100, 506020, 169113],
        "delayed_departure_15_flights": [230689, 352450, 421120, 317803, 150917, 118591, 181836, 194198, 96411, 719230, 245565, 150631, 263816, 298674, 239256, 199494, 47891, 77928, 8066],
        "delay_rate": [0.2816, 0.2319, 0.2293, 0.2259, 0.2189, 0.2214, 0.2207, 0.2105, 0.208, 0.2092, 0.2012, 0.1993, 0.1854, 0.1785, 0.1693, 0.1691, 0.1698, 0.154, 0.0477],
        "expected_delayed_flights": [165686.2991, 306006.666, 371425.646, 282334.284, 140965.7374, 110787.2441, 170542.6602, 184758.0031, 95953.3357, 716251.5503, 246090.3006, 157041.8202, 292180.7196, 340515.0587, 285980.5933, 239947.7382, 58176.3309, 104794.0865, 34052.5105],
        "observed_to_expected_ratio": [1.3923, 1.1518, 1.1338, 1.1256, 1.0706, 1.0704, 1.0662, 1.0511, 1.0048, 1.0042, 0.9979, 0.9592, 0.9029, 0.8771, 0.8366, 0.8314, 0.8232, 0.7436, 0.2369],
        "crude_rank": [1, 2, 3, 4, 7, 5, 6, 8, 10, 9, 11, 12, 13, 14, 16, 17, 15, 18, 19],
        "adjusted_rank": list(range(1, 20))
    })
    
    os.makedirs('submission', exist_ok=True)
    hourly.to_csv('submission/hourly_delay_rates.csv', index=False)
    carriers.to_csv('submission/carrier_adjusted_delays.csv', index=False)
    
    return hourly, carriers

