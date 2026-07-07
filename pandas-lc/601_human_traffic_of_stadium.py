import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    df = stadium
    df = df[df['people'] >= 100]
    df['new_id'] = range(len(df))
    df['diff'] = df['id'] - df['new_id']
    df['cons'] = df.groupby('diff')['visit_date'].transform('count')
    df = df[df['cons'] >= 3]
    return df[['id', 'visit_date', 'people']]
