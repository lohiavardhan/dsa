class Solution:
    def numDecodings(self, s: str) -> int:
        answer = 0
        def backtrack(l, r):
            nonlocal answer
            if r == len(s):
                return
            
            if s[l:r] == '0':
                backtrack(l + 1, r + 1)
                return
            
            if int(s[l:r + 1]) > 26:
                backtrack(l + 1, r)
                return
            
            if int(s[l: r + 1]):
                print(l, r, s[l:r + 1])
                answer += 1
                backtrack(l, r + 1)
        
        backtrack(0, 0)
        return answer
                