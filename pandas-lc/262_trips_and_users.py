import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(trips, users, left_on='client_id', right_on='users_id', how='outer')
    df = pd.merge(df, users, left_on='driver_id', right_on='users_id', how='inner')
    df.drop(columns=['users_id_x', 'role_x', 'users_id_y', 'role_y'], inplace=True)
    df['Date'] = pd.to_datetime(df['request_at'])
    df = df[(df['Date'] >= pd.to_datetime('2013-10-01')) & (df['Date'] <= pd.to_datetime('2013-10-03'))]
    df['allowed'] = ~((df['banned_x'] == 'Yes') | (df['banned_y'] == 'Yes'))
    df = df[df['allowed']]
    df['total count'] = df.groupby('request_at')['id'].transform('count')
    df['cancel count'] = df.groupby('request_at')['status'].transform(lambda x: x.str.startswith('cancel').sum())

    df['Cancellation Rate'] = round(df['cancel count'] / df['total count'], 2)
    df.rename(columns={'request_at' : 'Day'}, inplace=True)
    df.drop_duplicates(subset=['Day'], inplace=True)
    return df[['Day', 'Cancellation Rate']]
