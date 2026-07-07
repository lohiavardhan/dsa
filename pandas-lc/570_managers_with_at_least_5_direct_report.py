import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee
    df['manager_s_count'] = df.groupby('managerId')['managerId'].transform('count')
    df2 = df[df['manager_s_count'] >= 5]
    df2 = df2.drop_duplicates(subset=['managerId'])
    managers = set(df2['managerId'])
    
    df = df[df['id'].isin(managers)]

    return df[['name']]