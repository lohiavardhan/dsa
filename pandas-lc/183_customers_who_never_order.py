import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    never_order_df = pd.merge(orders, customers, left_on='customerId', right_on='id', how='inner')
    never_order_set = set(never_order_df['customerId'])
    df = customers[~customers['id'].isin(never_order_set)]
    df['Customers'] = df['name']
    return df[['Customers']]