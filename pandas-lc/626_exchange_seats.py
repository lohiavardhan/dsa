import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    df = seat
    for i in range(0, len(seat) - 1, 2):
        df.iloc[i, 1], df.iloc[i + 1, 1] = df.iloc[i + 1, 1], df.iloc[i, 1]
    
    return df
