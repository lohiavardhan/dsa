import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers.drop_duplicates(subset=['num'], keep=False, inplace=True)

    return pd.DataFrame({'num' : [my_numbers['num'].max()]})
