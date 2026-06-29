class Solution:
    def climbStairs(self, n: int) -> int:

        answer = 0

        def dfs(rem, curr_steps):
            nonlocal answer
            if rem < 2:
                answer = answer + 1
                return
            
            dfs(rem - 1, curr_steps + 1)
            dfs(rem - 2, curr_steps + 1)
        
        dfs(n, 0)
        return answer
        