class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        dp = {}

        def dfs(i, bought):
            if (i, bought) in dp:
                return dp[(i, bought)]
            if i >= len(prices):
                return 0
            
            if bought == float('inf'):
                profit = max(dfs(i + 1, prices[i]), dfs(i + 1, bought))

            else:
                profit = dfs(i + 1, bought)
                if prices[i] > bought:
                    profit = max(profit, (prices[i] - bought) + dfs(i + 2, float('inf')))
            
            dp[(i, bought)] = profit
            return profit
        
        return dfs(0, float('inf'))