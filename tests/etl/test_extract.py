import os

import pandas as pd
from dotenv import load_dotenv

from etl.extract import extract_csv

load_dotenv()

RAW_DATA_PATH = os.getenv("RAW_DATA_PATH")

def test_extract_csv():
    df = extract_csv(str(RAW_DATA_PATH))

    assert isinstance(df, pd.DataFrame)
    assert not df.empty