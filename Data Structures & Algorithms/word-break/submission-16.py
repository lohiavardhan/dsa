class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for _ in range(len(s) + 1)]
        dp[len(s)] = True

        i = len(s) - 1
        while i >= 0:
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break
            i -= 1
        
        return dp[0]