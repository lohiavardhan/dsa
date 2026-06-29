class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        j = 0
        i = 0
        while j <= len(s) - 1:
            if s[i:j + 1] in wordDict:
                i = j + 1
                j = j + 1
               
            else:
                j = j + 1
        
        print(s[i:j + 1], i, j)
        if i == j:
            return True
        else:
            return False