class Solution:
    def climbStairs(self, n: int) -> int:
        
        res = [0 for _ in range(n + 1)]
        res[1] = 1
        res[2] = 2

        for i in range(3, len(res)):
            res[i] = res[i - 1] + res[i - 2]
        
        print(res)
        return res[n]