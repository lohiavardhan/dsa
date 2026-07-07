import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    df = logs
    df['var'] = df['num'].rolling(window=3).var()
    df = df[df['var'] == 0]
    df = df.drop_duplicates(subset=['num'])
    df['ConsecutiveNums'] = df['num']
    return df[['ConsecutiveNums']]