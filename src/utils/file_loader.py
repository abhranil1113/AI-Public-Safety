import os
import pandas as pd
from src.utils.constants import (
    SCAM_DATA_DIR,
    CURRENCY_DATA_DIR,
    TRANSACTIONS_DATA_DIR,
    COMPLAINTS_DATA_DIR,
    GEOSPATIAL_DATA_DIR
)
from src.utils.logger import setup_logger

logger = setup_logger("FileLoader")

def load_scam_calls() -> pd.DataFrame:
    path = os.path.join(SCAM_DATA_DIR, "scam_calls.csv")
    if not os.path.exists(path):
        logger.error(f"Scam calls file not found at {path}")
        return pd.DataFrame()
    return pd.read_csv(path)

def load_sample_scam_inputs() -> pd.DataFrame:
    path = os.path.join(SCAM_DATA_DIR, "sample_scam_inputs.csv")
    if not os.path.exists(path):
        logger.error(f"Sample scam inputs not found at {path}")
        return pd.DataFrame()
    return pd.read_csv(path)

def load_currency_metadata() -> pd.DataFrame:
    path = os.path.join(CURRENCY_DATA_DIR, "metadata.csv")
    if not os.path.exists(path):
        logger.error(f"Currency metadata not found at {path}")
        return pd.DataFrame()
    return pd.read_csv(path)

def load_transactions() -> pd.DataFrame:
    path = os.path.join(TRANSACTIONS_DATA_DIR, "transactions.csv")
    if not os.path.exists(path):
        logger.error(f"Transactions file not found at {path}")
        return pd.DataFrame()
    return pd.read_csv(path)

def load_complaints() -> pd.DataFrame:
    path = os.path.join(COMPLAINTS_DATA_DIR, "complaints.csv")
    if not os.path.exists(path):
        logger.error(f"Complaints file not found at {path}")
        return pd.DataFrame()
    return pd.read_csv(path)

def load_geospatial_districts() -> pd.DataFrame:
    path = os.path.join(GEOSPATIAL_DATA_DIR, "crime_districts.csv")
    if not os.path.exists(path):
        logger.error(f"Geospatial districts not found at {path}")
        return pd.DataFrame()
    return pd.read_csv(path)

def load_district_coordinates() -> pd.DataFrame:
    path = os.path.join(GEOSPATIAL_DATA_DIR, "district_coordinates.csv")
    if not os.path.exists(path):
        logger.error(f"District coordinates not found at {path}")
        return pd.DataFrame()
    return pd.read_csv(path)
