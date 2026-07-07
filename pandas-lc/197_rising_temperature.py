import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['Date'] = pd.to_datetime(weather['recordDate'])
    weather = weather.sort_values(by=['Date'], ascending=True)
    weather['Next Date'] = weather['Date'] + pd.Timedelta(days=1)
    df = pd.merge(weather, weather, left_on='Next Date', right_on='Date', how='outer')
    
    df = df[['id_y', 'Date_x', 'Date_y', 'temperature_x', 'temperature_y']]
    print(df)

    df = df[(df['temperature_y'] > df['temperature_x'])]
    df.rename(columns={'id_y' : 'id'}, inplace=True)
    return df[['id']]