class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = {len(s) : True}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            dp[i] = False
            for word in wordDict:
                candidate = i + len(word)
                
                if candidate <= len(s) and s[i:candidate] == word and dfs(candidate):
                    dp[i] = True
                    break
                
            return dp[i]
        
        
        dfs(0)
        return dp[0]