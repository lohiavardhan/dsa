class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordlist = set(wordDict)

        r = len(s) - 1

        for l in range(r, -1, -1):
            if s[l:r + 1] in wordlist:
                r = l - 1
            
        return r == -1