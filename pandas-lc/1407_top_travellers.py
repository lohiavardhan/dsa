import pandas as pd
import numpy as np
def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(users, rides, left_on='id', right_on='user_id', how='left').fillna(0)
    df['travelled_distance'] = df.groupby('user_id')['distance'].transform('sum')
    df.sort_values(by=['name'], ascending=True, inplace=True)
    df.sort_values(by=['travelled_distance'], ascending=False, inplace=True)
    df.drop_duplicates(subset=['user_id'], inplace=True)
    
    return df[['name', 'travelled_distance']]
