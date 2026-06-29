class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        answer = 0
        l = 0
        hashmap = defaultdict(int)

        for r in range(len(s)):
            hashmap[s[r]] += 1
            max_freq = max(hashmap.values())

            if r - l + 1 > max_freq + k:
                hashmap[s[l]] -= 1
                l += 1
            
            answer = max(answer, r - l + 1)


        return answer