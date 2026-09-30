import pandas as pd

def extract_csv(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns its contents as a pandas DataFrame.
    """
    return pd.read_csv(file_path)