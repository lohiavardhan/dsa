import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views1 = views
    views2 = views

    df = views[views['author_id'] == views['viewer_id']]
    df = df.drop_duplicates(subset=['viewer_id'], keep='first')
    df['id'] = df['viewer_id']
    df = df.sort_values(by='id')
    return df[['id']]