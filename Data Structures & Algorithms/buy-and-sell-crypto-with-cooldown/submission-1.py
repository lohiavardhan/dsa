class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            
            static = dfs(i + 1, buy)
            if buy:
                res = dfs(i + 1, not buy) - prices[i]
                res = max(res, static)
            else:
                res = dfs(i + 2, not buy) + prices[i]
                res = max(res, static)
            
            dp[(i, buy)] = res
            return res
        
        return dfs(0, True)