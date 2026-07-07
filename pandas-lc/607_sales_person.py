import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    com_ord = pd.merge(company, orders, left_on='com_id', right_on='com_id', how='outer')
    full = pd.merge(com_ord, sales_person, left_on='sales_id', right_on='sales_id', how='outer')
    red_associated = full[full['name_x'] == 'RED']
    set_red = red_associated['name_y']
    full = full[~full['name_y'].isin(set_red)]
    full.drop_duplicates(subset=['name_y'], inplace=True)
    full.dropna(subset=['name_y'], inplace=True)
    full.rename(columns={'name_y' : 'name'}, inplace=True)

    return full[['name']]
