import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    df = triangle
    df['triangle'] = np.where((df['x'] + df['y'] > df['z']) & (df['z'] + df['y'] > df['x']) & (df['x'] + df['z'] > df['y']), 'Yes', 'No')
    return df
