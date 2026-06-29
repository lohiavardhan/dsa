class Solution:
    def climbStairs(self, n: int) -> int:

        array = [None for _ in range(n + 1)]
        array[n] = 1
        array[n- 1] = 1
        
        i = n - 2

        while i >= 0:
            array[i] = array[i + 1] + array[i + 2]
            i -= 1
        
        return array[0]

        