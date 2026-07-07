import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, bonus, left_on='empId', right_on='empId', how='left')
    df = df[(df['bonus'] < 1000) | (df['bonus'].isna())]
    return df[['name', 'bonus']]
