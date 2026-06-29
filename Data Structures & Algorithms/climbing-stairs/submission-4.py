class Solution:
    def climbStairs(self, n: int) -> int:

        one, two = 1, 1

        i = n - 2
        while i >= 0:
            one , two = one + two, one
            i -= 1
        
        return one

        