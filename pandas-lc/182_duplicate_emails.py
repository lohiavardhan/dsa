import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person[person.duplicated('email')]
    df.rename(columns={'email': 'Email'}, inplace=True)
    df.drop_duplicates(subset=['Email'], inplace=True)
    return df[['Email']]