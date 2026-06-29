class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        l, r = 0, 1
        minPrice = 10000

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            
            answer = max(answer, prices[r] - prices[l])
            r += 1

        return answer