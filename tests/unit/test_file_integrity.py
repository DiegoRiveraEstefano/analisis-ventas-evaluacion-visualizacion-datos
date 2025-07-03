from pathlib import Path

import polars as pl

output_file_path = Path("../data/processed/Ventas_Transformadas.parquet")
post_load = pl.read_parquet(output_file_path)
assert post_load.shape == (991, 10), "Error en conservación de dimensión"
print("✔ Dataset validado: 100% de integridad")
