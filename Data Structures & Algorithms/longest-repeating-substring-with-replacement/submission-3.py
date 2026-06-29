class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        hashmap = {}
        max_size = 0
        for r in range(len(s)):
            curr_window = s[l:r + 1]
            
            most_frequent_amount = 0

            for (key, value) in hashmap.items():
                if value > most_frequent_amount:
                    most_frequent_amount = value
            
            
            max_size = len(curr_window)

            if len(curr_window) > most_frequent_amount + k:
                l += 1
                hashmap[s[l]] -= 1
            
            max_size = max(max_size, len(curr_window))
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
        
        return max_size
            
