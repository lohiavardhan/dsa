import pandas as pd
import numpy as np

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    df = accounts
    df['Cat'] = np.where(df['income'] > 50000, 2, np.where(df['income'] < 20000, 0, 1))
    df['count'] = df.groupby('Cat')['Cat'].transform('count')
    df = df.drop_duplicates(subset=['Cat'])
    low_count = int(df[df['Cat'] == 0]['count']) if len(df[df['Cat'] == 0]) else 0
    average_count = int(df[df['Cat'] == 1]['count']) if len(df[df['Cat'] == 1]) else 0
    high_count = int(df[df['Cat'] == 2]['count']) if len(df[df['Cat'] == 2]) else 0

    answer = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_count, average_count, high_count] 
        })
    return answer