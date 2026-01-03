import pandas as pd
from sklearn.preprocessing import LabelEncoder
import yaml
import logging

import sys
import os
from pathlib import Path

ROOT = Path().resolve()
sys.path.append(str(ROOT))

print(ROOT)

CONFIG_PATH = os.path.join(ROOT,"configs","config.yaml")

config = yaml.safe_load(open(CONFIG_PATH))

LOG_DIR = os.path.join(ROOT,"logs")

LOG_FILE_PATH = os.path.join(LOG_DIR,"app.log")

logging.basicConfig(
    filename=str(LOG_FILE_PATH),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s',
    filemode='a'  # Append mode
)

logging.info("Logging system initialized")
logging.info(f"Project root: {ROOT}")

DATA_PATH = os.path.join(ROOT,"data","crop_fertilizer.csv")

def load_data():
    df = pd.read_csv(DATA_PATH)
    df = df.drop(columns=['District_Name'], errors='ignore')
    logging.info(f"Data loaded successfully from {DATA_PATH}")
    logging.info(f"Dataset shape: {df.shape}")
    return df

def encode_data(df):
    label_encoders = {}
    for col in ['Soil_color', 'Crop', 'Fertilizer']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    logging.info("Categorical columns encoded")
    return df, label_encoders

if __name__ == "__main__":
    print(f"Project Root: {ROOT}")
    print(f"Config File: {CONFIG_PATH}")
    print(f"Log File: {LOG_FILE_PATH}")
    print(f"Data File: {DATA_PATH}")
    
    # Test loading
    try:
        df = load_data()
        print(f"\nLoaded {len(df)} rows successfully!")
        print("Columns:", df.columns.tolist())
    except Exception as e:
        print(f"Error loading data: {e}")