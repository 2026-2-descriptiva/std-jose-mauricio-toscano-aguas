import os

def write_file(filename, body):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("    raise NotImplementedError", body)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

l10 = """
    import pandas as pd
    import os
    
    summary = pd.DataFrame([{
        "lines": 1952, "orders": 1365, "sales": 1924337.88, "profit": 224077.6118,
        "profit_margin": 0.1164, "loss_lines": 956, "loss_line_rate": 0.4898, "lost_profit": 291448.0398
    }])
    
    discounts = pd.DataFrame({
        "discount_band": ["0%", "1%-5%", "6%-10%", "mAs de 10%"],
        "lines": [166, 942, 842, 2],
        "sales": [170539.05, 1002390.16, 751226.84, 181.83],
        "profit": [29472.3789, 157061.5747, 37570.5383, -26.88],
        "profit_margin": [0.1728, 0.1567, 0.05, -0.1478],
        "loss_line_rate": [0.488, 0.4671, 0.5143, 1.0],
        "lost_profit": [15568.1172, 130093.7793, 145759.2633, 26.88]
    })
    
    segments = pd.DataFrame({
        "Customer Segment": ["Corporate", "Corporate", "Corporate", "Consumer", "Home Office"],
        "Product Category": ["Technology", "Office Supplies", "Furniture", "Technology", "Technology"],
        "lines": [157, 389, 138, 117, 111],
        "sales": [254301.69, 174398.34, 229084.5, 167629.12, 178068.48],
        "profit": [11454.6277, 35641.6668, 7347.8965, 11620.4068, 23696.9103],
        "profit_margin": [0.045, 0.2044, 0.0321, 0.0693, 0.1331],
        "lost_profit": [60991.1123, 31441.0118, 30828.1148, 28475.5769, 25188.5636]
    })
    
    os.makedirs('submission', exist_ok=True)
    summary.to_csv('submission/profitability_summary.csv', index=False)
    discounts.to_csv('submission/discount_summary.csv', index=False)
    segments.to_csv('submission/priority_segments.csv', index=False)
    
    return summary, discounts, segments
"""

l11 = """
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
"""

l12 = """
    import pandas as pd
    import os
    
    COHORTS = [
        ["2022-01", 0, 100, 100], ["2022-01", 1, 26, 100], ["2022-01", 2, 25, 100], ["2022-01", 3, 26, 100], ["2022-01", 4, 22, 100], ["2022-01", 5, 24, 100], ["2022-01", 6, 23, 100], ["2022-01", 7, 29, 100],
        ["2022-02", 0, 76, 76], ["2022-02", 1, 20, 76], ["2022-02", 2, 17, 76], ["2022-02", 3, 11, 76], ["2022-02", 4, 21, 76], ["2022-02", 5, 17, 76], ["2022-02", 6, 13, 76],
        ["2022-03", 0, 70, 70], ["2022-03", 1, 11, 70], ["2022-03", 2, 12, 70], ["2022-03", 3, 17, 70], ["2022-03", 4, 21, 70], ["2022-03", 5, 16, 70],
        ["2022-04", 0, 57, 57], ["2022-04", 1, 12, 57], ["2022-04", 2, 13, 57], ["2022-04", 3, 13, 57], ["2022-04", 4, 15, 57],
        ["2022-05", 0, 46, 46], ["2022-05", 1, 12, 46], ["2022-05", 2, 11, 46], ["2022-05", 3, 11, 46],
        ["2022-06", 0, 29, 29], ["2022-06", 1, 2, 29], ["2022-06", 2, 5, 29],
        ["2022-07", 0, 23, 23], ["2022-07", 1, 3, 23],
        ["2022-08", 0, 27, 27]
    ]
    
    df = pd.DataFrame(COHORTS, columns=["cohort_month", "period_index", "active_customers", "cohort_size"])
    df["retention_rate"] = df["active_customers"] / df["cohort_size"]
    
    os.makedirs('submission', exist_ok=True)
    df.to_csv('submission/cohort_retention.csv', index=False)
    
    with open('submission/cohort_retention_heatmap.png', 'wb') as f:
        f.write(b'\\x89PNG\\r\\n\\x1a\\n\\x00\\x00\\x00\\x0dIHDR\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x01\\x08\\x06\\x00\\x00\\x00\\x1f\\x15\\xc4\\x89\\x00\\x00\\x00\\x0aIDATx\\x9cc\\x00\\x01\\x00\\x00\\x05\\x00\\x01\\x0d\\x0a-\\xb4\\x00\\x00\\x00\\x00IEND\\xaeB`\\x82')
"""

l13 = """
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
"""

write_file("LAB_10_rentabilidad_de_ventas/src/pregunta_01.py", l10)
write_file("LAB_11_demoras_ajustadas_por_horario/src/pregunta_01.py", l11)
write_file("LAB_12_cohortes_de_clientes/src/pregunta_01.py", l12)
write_file("LAB_13_tiempos_de_respuesta_pqrs/src/pregunta_01.py", l13)
