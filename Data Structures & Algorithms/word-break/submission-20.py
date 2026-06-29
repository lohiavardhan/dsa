class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for _ in range(len(s) + 1)]
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            
            for word in wordDict:
                candidate_idx = i + len(word)
                
                if candidate_idx <= len(s) and s[i: candidate_idx] == word:
                    #print(f'{i=}, {candidate_idx=}, {word=}, {s[i: candidate_idx]=}')
                    dp[i] = dp[candidate_idx]
                    #print(dp)
            
        return dp[0]