class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        answer = ""

        for i in range(len(s)):
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                string = s[l:r + 1]
                if len(string) > len(answer):
                    answer = string
                
                l -= 1
                r += 1
            
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                string = s[l:r + 1]
                if len(string) > len(answer):
                    answer = string
                
                l -= 1
                r += 1


        return answer