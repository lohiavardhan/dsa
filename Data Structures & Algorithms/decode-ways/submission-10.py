class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0 for _ in range(len(s) + 1)]

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1] if dp[i + 1] else 1
                if (s[i] == '1' or s[i] == '2') and i < len(s) - 1 and '0' < s[i + 1] <= '6':
                    dp[i] = dp[i] + 1   
      

            
        
        return dp[0]