class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        amount = 0
        stock = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            if prices[r] > prices[l]:
                amount += prices[r] - prices[l]
                l = r

        return amount