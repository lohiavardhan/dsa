import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    employee = employee[employee['rank'] <= 3]

    df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='inner')
    df.rename(columns={'name_x' : 'Employee', 'name_y' : 'Department', 'salary' : 'Salary'}, inplace=True)

    return df[['Department', 'Employee', 'Salary']]