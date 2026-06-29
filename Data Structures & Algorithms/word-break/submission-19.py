class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False for _ in range(len(s))]
        
        def dfs(l, r):
            if r >= len(s):
                return True

            #print(f'{l=}, {r=}, {s[l:r + 1]= }')
            
            if s[l: r + 1] in wordDict:
                #print(f'MATCH {s[l: r + 1]=}')
                dp[r] = True
                dfs(l, r + 1) or dfs(r + 1, r + 1)
            else:
                dfs(l, r + 1)
            
            return False

        
        dfs(0, 0)
        #print(dp)

        return dp[-1]