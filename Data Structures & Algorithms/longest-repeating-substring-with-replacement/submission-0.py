class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        hashmap = defaultdict(int)
        l = 0

        for r in range(len(s)):

            hashmap[s[r]] += 1
            print(hashmap, r, s[r], l, s[l])
            
            most_freq = 0
            for (key, value) in hashmap.items():
                most_freq = max(most_freq, value)
            
            if (r - l + 1) - most_freq > k:
                print(r, l, most_freq, hashmap, s[l], k)
                hashmap[s[l]] -= 1
                l += 1

            
            
            res = max(res, r - l + 1)

        


        return res