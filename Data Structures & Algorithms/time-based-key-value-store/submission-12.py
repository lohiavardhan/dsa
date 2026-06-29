class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dictionary:
            self.dictionary[key].append((timestamp, value))
        else:
            self.dictionary[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        
        search_space = self.dictionary[key]
        print(len(search_space), search_space)
        
        l = 0 
        r = len(search_space) - 1

        res = ""

        while l <= r:
            mid = (l + r) // 2

            if timestamp > search_space[mid][0]:
                res = search_space[mid][1]
                l = mid + 1
            elif timestamp < search_space[mid][0]:
                r = mid - 1
            else:
                return search_space[mid][1]
        
        return res


