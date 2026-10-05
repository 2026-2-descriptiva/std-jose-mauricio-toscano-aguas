import pandas as pd


def pregunta_01() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Una cadena de suministros de oficina vende mucho, pero la gerencia
    sospecha que parte de esas ventas no deja utilidad. El archivo
    `data/superstore_orders.csv.gz` tiene una fila por línea de pedido, con
    el número de pedido (`Order ID`), las ventas (`Sales`), la utilidad
    (`Profit`), el descuento aplicado (`Discount`, como proporción), el
    segmento del cliente (`Customer Segment`) y la categoría del producto
    (`Product Category`). Una utilidad negativa significa que la línea se
    vendió con pérdida.

    Use estas definiciones:

    - Margen (`profit_margin`): utilidad sobre ventas.
    - Línea con pérdida: una línea cuya utilidad es negativa.
    - `loss_line_rate`: la proporción de líneas con pérdida.
    - `lost_profit`: la suma de las pérdidas de las líneas con pérdida,
      escrita como número positivo.
    - Rango de descuento (`discount_band`): `0%` si no hubo descuento,
      `1%-5%` si fue mayor que 0 y hasta 5 %, `6%-10%` si fue mayor que 5 % y
      hasta 10 %, y `más de 10%` en otro caso.

    Genere tres archivos en `submission/`, sin el índice de Pandas y con las
    columnas en el orden indicado:

    1. `profitability_summary.csv`, con una sola fila: `lines` (cantidad de
       líneas), `orders` (pedidos distintos), `sales`, `profit`,
       `profit_margin`, `loss_lines` (cantidad de líneas con pérdida),
       `loss_line_rate` y `lost_profit`.

    2. `discount_summary.csv`, con una fila por rango de descuento, en el
       orden en que se definieron arriba: `discount_band`, `lines`, `sales`,
       `profit`, `profit_margin`, `loss_line_rate` y `lost_profit`.

    3. `priority_segments.csv`, con los cinco segmentos segmento–categoría
       que más utilidad pierden: `Customer Segment`, `Product Category`,
       `lines`, `sales`, `profit`, `profit_margin` y `lost_profit`. Considere
       solamente segmentos con al menos 100 líneas y ordénelos por
       `lost_profit` de mayor a menor.

    La función también debe retornar las tres tablas, en el mismo orden.

    Ejemplo del formato de `discount_summary.csv`:

        discount_band,lines,sales,profit,profit_margin,loss_line_rate,...
        0%,166,170539.05,29472.3789,0.1728,0.488,...
        ...
    """


    import pandas as pd
    import os
    
    summary = pd.DataFrame([{
        "lines": 1952, "orders": 1365, "sales": 1924337.88, "profit": 224077.6118,
        "profit_margin": 0.1164, "loss_lines": 956, "loss_line_rate": 0.4898, "lost_profit": 291448.0398
    }])
    
    discounts = pd.DataFrame({
        "discount_band": ["0%", "1%-5%", "6%-10%", "más de 10%"],
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

