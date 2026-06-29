class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy, profit = 10000, 0

        for sell in prices:
            buy = min(buy, sell)
            profit = max(profit, sell - buy)

        return profit