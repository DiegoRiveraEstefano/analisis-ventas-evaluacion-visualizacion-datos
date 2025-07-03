import polars as pl


def clean_data(df: pl.DataFrame) -> pl.DataFrame:
    df_ventas_pl = df.with_columns(
        # 1. Conversión de tipos de datos
        # Convertir 'fecha_venta' a datetime
        pl.col("fecha_venta")
        .str.strptime(pl.Date, format="%d/%m/%Y", strict=False)
        .alias("fecha_venta"),
        # Limpiar y convertir 'precio_unitario' a numérico (float)
        pl.col("precio_unitario")
        .str.replace(" €", "")
        .str.replace(",", ".", literal=True)
        .str.replace(" ", "", n=2)
        .cast(pl.Float64)
        .alias("precio_unitario"),
        # Convertir 'cantidad' a numérico
        pl.col("cantidad").cast(pl.Int64).alias("cantidad"),
    )
    df_ventas_pl = df_ventas_pl.with_columns(
        pl.when(pl.col("producto") == "")
        .then(pl.lit(None, pl.String))
        .otherwise(pl.col("producto"))
        .alias("producto")
    )
    # Ahora llenar los nulos en 'producto'
    df_ventas_pl = df_ventas_pl.with_columns(
        pl.col("producto").fill_null("Desconocido").alias("producto")
    )
    # Eliminar filas con nulos en columnas críticas después de la transformación
    print("\n--- Manejo de valores nulos (Imputación por Media/Moda) ---")

    # Columnas numéricas para imputar con la media
    numeric_cols_to_impute = ["precio_unitario", "cantidad"]

    for col in numeric_cols_to_impute:
        if df_ventas_pl[col].null_count() <= 0:
            continue  # Si no hay nulos, saltar

        # Calcular la media de la columna
        mean_value = df_ventas_pl[col].mean()
        # Imputar los valores nulos con la media calculada
        df_ventas_pl = df_ventas_pl.with_columns(
            pl.col(col).fill_null(mean_value).alias(col)
        )
        print(f"Valores nulos en '{col}' imputados con la media ({mean_value:.2f}).")

    # Columnas categóricas para imputar con la moda
    categorical_cols_to_impute = [
        "region"
    ]  # Añade aquí otras columnas categóricas si es necesario

    for col in categorical_cols_to_impute:
        if df_ventas_pl[col].null_count() <= 0:
            continue  # Si no hay nulos, saltar

        # Calcular la moda (valor más frecuente) de la columna
        # Polars tiene un método `mode()`. Si hay múltiples modas, toma la primera.
        mode_value = (
            df_ventas_pl.group_by(col)
            .len()
            .sort(by="len", descending=True)
            .select(col)
            .head(1)
            .item()
        )

        # Imputar los valores nulos con la moda calculada
        df_ventas_pl = df_ventas_pl.with_columns(
            pl.col(col).fill_null(mode_value).alias(col)
        )
        print(f"Valores nulos en '{col}' imputados con la moda ('{mode_value}').")

    initial_rows_before_date_dropna = df_ventas_pl.shape[0]
    df_ventas_pl = df_ventas_pl.drop_nulls(subset=["fecha_venta"])
    rows_removed_date_nulls = initial_rows_before_date_dropna - df_ventas_pl.shape[0]

    if rows_removed_date_nulls > 0:
        print(
            f"Se eliminaron {rows_removed_date_nulls} filas con valores nulos en 'fecha_venta' (después de intentar la conversión)."
        )

    print("\nValores nulos después de la imputación/eliminación final:")
    print(
        df_ventas_pl.null_count()
    )  # Usar .null_count() en Polars para ver los nulos por columna

    # 4. Tratamiento de valores atípicos (ej: cantidad = 0)
    initial_rows_before_zero = df_ventas_pl.shape[0]
    df_ventas_pl = df_ventas_pl.filter(pl.col("cantidad") > 0)
    rows_removed_zero_qty = initial_rows_before_zero - df_ventas_pl.shape[0]
    if rows_removed_zero_qty > 0:
        print(
            f"Se eliminaron {rows_removed_zero_qty} filas donde 'cantidad' era igual o menor a 0."
        )

    return df_ventas_pl
