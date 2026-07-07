import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salary = employee.groupby('departmentId')['salary'].transform('max')
    df = employee[employee['salary'] == max_salary]
    
    
    answer_df = pd.merge(df, department, left_on='departmentId', right_on='id', how='inner')
    answer_df = answer_df.rename(columns={'name_y' : 'Department', 'name_x': 'Employee', 'salary' : 'Salary'})
    return answer_df[['Department', 'Employee', 'Salary']]