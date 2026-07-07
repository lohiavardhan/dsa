import pandas as pd
import numpy as np

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, employee, left_on='managerId', right_on='id', how='inner')
    df = df[df['salary_x'] > df['salary_y']]
    df['Employee'] = df['name_x']

    return df[['Employee']]