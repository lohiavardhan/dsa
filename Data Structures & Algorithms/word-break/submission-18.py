class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(l, r):
            if r >= len(s):
                return True
            
            if s[l: r] in wordDict:
                return dfs(l, r + 1) or dfs(l + 1, r + 1)
            else:
                return dfs(l, r + 1)

        return dfs(0, 0)