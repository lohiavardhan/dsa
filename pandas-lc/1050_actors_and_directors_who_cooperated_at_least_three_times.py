import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director
    df['count'] = df.groupby(['actor_id', 'director_id'])['timestamp'].transform('count')
    df = df[df['count'] >= 3]
    df.drop_duplicates(subset=['actor_id', 'director_id'], inplace=True)
    return df[['actor_id', 'director_id']]
