import os
import sys
import pandas as pd
from datetime import datetime

"""
Defining common constant variable for training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFICAT_DIR: str = "Artificats"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


SCHEMA_FILE_PATH  =    os.path.join("data_schema","schema.yaml")

"""
Data Ingestion related constant start with Data_INGESTION var name
"""

DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "memesashishAi"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_NAME: str = "feature_store"
DATA_INGESTION_INGESTION_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = 'data_validation'
DATA_VALIDATION_VALID_NAME: str = 'validation'
DATA_VALIDATION_INVALID_NAME: str = 'invalid'
DATA_VALIDATION_DRIFT_NAME: str = 'drift_report'
DATA_VALIDATION_REPORT_NAME: str = 'report.yaml'