import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates('salary')
    if len(employee) < 2:
        return pd.DataFrame({"SecondHighestSalary" : [None]})
    
    df = employee.nlargest(2, 'salary')
    return pd.DataFrame({"SecondHighestSalary" : [df.iloc[1]['salary']]})