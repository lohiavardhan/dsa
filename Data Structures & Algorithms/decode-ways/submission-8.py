class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [1 for _ in range(len(s) + 1)]

        print(dp)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if s[i] == '1' or s[i] == '2' and i < len(s) - 1 and s[i + 1] <= '6':
                    dp[i] = dp[i] + 1            

            print(dp)
        
        return dp[0]