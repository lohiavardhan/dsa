import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders['order_count'] = orders.groupby('customer_number')['order_number'].transform('count')
    customer = orders[orders['order_count'] == orders['order_count'].max()]
    customer = customer.drop_duplicates(subset=['customer_number'])
    return customer[['customer_number']]
