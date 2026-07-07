import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses
    df['count'] = df.groupby('class')['student'].transform('count')
    df = df[df['count'] >= 5]
    df.drop_duplicates(subset=['class'], inplace=True)
    return df[['class']]
