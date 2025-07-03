from pathlib import Path

RAW_DATA_FILE_NAME = "Ventas.csv"

CLEAN_DATA_FILE_NAME = "cleaned_data.parquet"

TRANSFORMED_DATA_FILE_NAME = "transformed_data.parquet"

# Data paths

DATA_PATH = Path("data")

RAW_DATA_PATH = DATA_PATH / "raw"

PROCESSED_DATA_PATH = DATA_PATH / "processed"


# Reports paths

REPORTS_PATH = Path("reports")

REPORT_FIGURES_PATH = REPORTS_PATH / "figures"

REPORTS_PDFS_PATH = REPORTS_PATH / "pdfs"
