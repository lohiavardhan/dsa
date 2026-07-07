import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients
    df = df[df['conditions'].str.contains('^DIAB1| DIAB1', na=False)]
    return df
