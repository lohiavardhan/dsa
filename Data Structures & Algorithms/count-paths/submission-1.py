class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = {}
        dp[(m - 1, n - 1)] = 1
        dp[(m - 2, n - 1)] = 1
        dp[(m - 1, n - 2)] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[(i, j)] = dp.get((i + 1, j), 1) + dp.get((i, j + 1), 1)
        
        return dp[(0,0)]