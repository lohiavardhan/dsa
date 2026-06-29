class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if not amount:
            return 0

        min_list = [math.inf for n in range(amount + 1)]

        for c in coins:
            min_list[c] = 1
        
        for i in range(1, amount + 1):
            for c in coins:
                if i - c > 0:
                    min_list[i] = min(min_list[i - c] + 1, min_list[i])
        
        if min_list[amount] == math.inf:
            return -1
        

        return min_list[amount]