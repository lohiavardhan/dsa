class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = {}
        self.stack = collections.deque()

    def get(self, key: int) -> int:
        if key in self.stack:
            self.stack.remove(key)
            self.stack.append(key)
        return self.dictionary.get(key, -1)

    def put(self, key: int, value: int) -> None:

        
        self.dictionary[key] = value
        if key in self.stack:
            self.stack.remove(key)
        self.stack.append(key)
        
        if len(self.dictionary) > self.capacity:
            key_to_remove = self.stack.popleft()
            print(key_to_remove)
            del self.dictionary[key_to_remove]
        
