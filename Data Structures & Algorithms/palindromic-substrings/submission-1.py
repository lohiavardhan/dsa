class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0

        for i in range(len(s)):
            l, r = i, i
            change = 'l'
            while l >= 0 and r < len(s):
                print(i, s[i], l, s[l], r, s[r], change, answer)
                if s[l] == s[r]:
                    answer += 1
                if(change == 'l'):
                    l -= 1
                    change = 'r'
                    continue
                if(change == 'r'):
                    r += 1
                    change = 'l'
                
        return answer
        