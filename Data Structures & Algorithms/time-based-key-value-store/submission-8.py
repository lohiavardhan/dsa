class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dictionary:
            self.dictionary[key].append((timestamp, value))
        else:
            self.dictionary[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.dictionary:
            return ""
        search_space = list(self.dictionary[key])
        print(len(search_space), search_space)
        
        l = 0 
        r = len(search_space) - 1

        while l <= r:
            mid = (l + r) // 2

            if timestamp > search_space[mid][0]:
                l += 1
            elif timestamp < search_space[mid][0]:
                r -= 1
            else:
                return search_space[mid][1]
        
        print(mid, search_space[mid][0], timestamp, search_space[mid][1])
        if mid > 0 and timestamp < search_space[mid][0]:
            mid -= 1
        elif mid < len(search_space) - 1:
            # while mid < len(search_space) - 1 and timestamp > search_space[mid][0]:
            mid += 1

        print(mid, search_space[mid][0], timestamp, search_space[mid][1])
        return search_space[mid][1] if search_space[mid][0] < timestamp else ""


        
