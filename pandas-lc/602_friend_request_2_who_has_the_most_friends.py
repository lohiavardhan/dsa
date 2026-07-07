import pandas as pd
def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    res = defaultdict(int)
    for index, data in request_accepted.iterrows():
        res[data[0]] += 1
        res[data[1]] += 1
    
    maxim = max(res, key=res.get)
    
    return pd.DataFrame({'id' : [maxim], 'num' : [res[maxim]]})
