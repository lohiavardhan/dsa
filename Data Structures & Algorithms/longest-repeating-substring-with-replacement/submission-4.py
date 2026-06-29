class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        answer = 0
        hashmap = defaultdict(int)

        for r in range(len(s)):
            hashmap[s[r]] += 1

            max_freq = max(hashmap.values())

            if max_freq + k < (r - l + 1):
                hashmap[s[l]] -= 1
                l += 1
            
            answer = max(answer, r - l + 1)
        
        return answer
            
