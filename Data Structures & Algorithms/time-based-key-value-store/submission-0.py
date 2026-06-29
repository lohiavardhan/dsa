class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key] = (value, timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        


        return self.dictionary[key][0]
