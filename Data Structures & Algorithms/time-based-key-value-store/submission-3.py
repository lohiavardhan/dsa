class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[(key, timestamp)] = value
        

    def get(self, key: str, timestamp: int) -> str:
        
        search_space = list(self.dictionary.items())
        print(len(search_space), search_space)
        
        l = 0 
        r = len(search_space) - 1

        while l <= r:
            mid = (l + r) // 2

            if timestamp > search_space[mid][0][1]:
                l += 1
            elif timestamp < search_space[mid][0][1]:
                r -= 1
            else:
                return search_space[mid][1]
            
        print(mid, search_space[mid][0][1], search_space[mid][1])
        return search_space[mid][1] if search_space[mid][0][1] < timestamp else ""


        
