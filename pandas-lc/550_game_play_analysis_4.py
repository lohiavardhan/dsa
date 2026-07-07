import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity
    
    df['day_after_first'] = activity.groupby('player_id')['event_date'].transform('min') + pd.DateOffset(1)
    df = df[df['event_date'] == df['day_after_first']]
    print(df)
    next_day = df['player_id'].nunique()
    total_players = activity['player_id'].nunique()
    print(next_day)
    print(total_players)

    answer = round(next_day / total_players, 2)

    return pd.DataFrame({'fraction' : [answer]})