import pandas as pd

def dropMissingData(s: pd.DataFrame) -> pd.DataFrame:
    s.dropna(subset=['name'],inplace=True)
    return s
    