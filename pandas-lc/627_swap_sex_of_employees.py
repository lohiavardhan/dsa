import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    df = salary
    df['sex'] = np.where(df['sex'] == 'm', 'f', 'm')
    
    return df
