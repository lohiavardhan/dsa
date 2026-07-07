import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates('salary')
    if len(employee) < N or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    df = employee.nlargest(N, 'salary')
    row = df.iloc[N - 1]
    return pd.DataFrame({f'getNthHighestSalary({N})' : [row['salary']]})
