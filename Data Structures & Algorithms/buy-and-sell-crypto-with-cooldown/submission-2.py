class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 2)]

        for i in range(len(prices) - 1, -1, -1):
            for j in [True, False]:
                dp[i][j] = dp[i + 1][j]
                if j:
                    dp[i][j] = max(dp[i][j], dp[i + 1][not j] - prices[i])
                else:

                    dp[i][j] = max(dp[i][j], dp[i + 2][not j] + prices[i])

        return dp[0][1]