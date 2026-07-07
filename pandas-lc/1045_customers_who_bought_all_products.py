import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    
    products = len(product)
    customer = customer.drop_duplicates()
    customer['number_products'] = customer.groupby('customer_id')['product_key'].transform('count')
    customer = customer[customer['number_products'] >= products]
    customer.drop_duplicates(subset=['customer_id'], inplace=True)
    return customer[['customer_id']]
