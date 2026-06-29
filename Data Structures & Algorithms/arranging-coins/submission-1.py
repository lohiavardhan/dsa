class Solution:
    def arrangeCoins(self, n: int) -> int:

        
        stairs = 0
        used = 0

        for i in range(1, n):
            if used + i <= n:
                used += i
                stairs += 1
            else:
                break

        return stairs    
