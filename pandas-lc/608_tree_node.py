import pandas as pd
import numpy as np

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    df = tree
    df['type'] = np.where(df['p_id'].isna(), 'Root', None)
    df['type'] = np.where((df['id'].isin(df['p_id'])) & (df['type'].isna()), 'Inner', df['type'])
    df['type'] = np.where((df['type'].isna()), 'Leaf', df['type'])
    return df[['id', 'type']]
