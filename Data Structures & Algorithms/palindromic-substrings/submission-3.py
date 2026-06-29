class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0

        for i in range(len(s)):
            # ODD
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                answer += 1
                l -= 1
                r += 1
            
            # EVEN
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                answer += 1
                l -= 1
                r += 1
            
        return answer
        