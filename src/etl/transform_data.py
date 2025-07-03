import polars as pl


def transform_data(df: pl.DataFrame) -> pl.DataFrame:
    # Separar la fecha de venta en año, mes y día de la semana
    # Agregar columna 'valor_total_venta' a DataFrame
    df = df.with_columns(
        (pl.col("cantidad") * pl.col("precio_unitario")).alias("valor_total_venta")
    )

    # Separar la fecha de venta en año, mes y día de la semana
    df = df.with_columns(
        pl.col("fecha_venta").dt.year().alias("año_venta"),
        pl.col("fecha_venta").dt.month().alias("mes_venta"),
        pl.col("fecha_venta")
        .dt.weekday()
        .alias("dia_semana_num"),  # Lunes=1, Domingo=7
    )
    return df
