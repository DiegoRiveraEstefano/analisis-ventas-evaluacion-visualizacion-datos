from logging import getLogger

import polars as pl

from src.etl.clean_data import clean_data
from src.etl.transform_data import transform_data
from src.utils.const import (
    PROCESSED_DATA_PATH,
    RAW_DATA_FILE_NAME,
    RAW_DATA_PATH,
    TRANSFORMED_DATA_FILE_NAME,
)
from src.utils.logger import setup_logging
from src.visualization.visualization import make_plots

logger = getLogger(__name__)


def main():
    setup_logging()
    logger.info("Starting ETL process")

    logger.info(f"Reading raw data from {RAW_DATA_PATH / RAW_DATA_FILE_NAME}")
    df = pl.read_csv(
        RAW_DATA_PATH / RAW_DATA_FILE_NAME, encoding="windows-1252", separator=";"
    )

    logger.info("Raw data loaded successfully")
    logger.debug(f"Raw data shape: {df.shape}")
    df_cleaned = clean_data(df)

    logger.info("Data cleaned successfully")
    logger.debug(f"Cleaned data shape: {df_cleaned.shape}")

    logger.info("Transforming data")
    df_transformed = transform_data(df_cleaned)
    logger.info("Data transformed successfully")
    logger.debug(f"Transformed data shape: {df_transformed.shape}")

    logger.info("Making plots")
    make_plots(df_transformed)
    logger.info("ETL process completed successfully")

    logger.info("Saving transformed data to CSV")
    df_transformed.write_csv(PROCESSED_DATA_PATH / TRANSFORMED_DATA_FILE_NAME)
    logger.info("Data saved successfully")
    return 0


if __name__ == "__main__":
    main()
