class Solution:
    def isPalindrome(self, string):
            i = 0
            j = len(string) - 1

            while i < j:
                if(string[i] != string[j]):
                    return False
                i += 1
                j -= 1
            
            return True
    
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s
        if len(s) == 1:
            if(s[0] == s[1]):
                return s
            else:
                return s[0]

        if len(s) % 2 == 0:
            start_idx = len(s) // 2 - 1
            end_idx = start_idx + 2
        else:
            start_idx = len(s) // 2
            end_idx = start_idx + 1

        
        while self.isPalindrome(s[start_idx:end_idx]) and start_idx >= 0 and end_idx < len(s):
            start_idx -= 1
            end_idx += 1
            print(start_idx, end_idx, s[start_idx:end_idx], self.isPalindrome(s[start_idx:end_idx]))
            
        start_idx += 1
        end_idx -= 1
        return s[start_idx:end_idx]

        