class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # memo = {}

        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     if i >= len(nums) - 1:
        #         return True
        #     if nums[i] == 0:
        #         return False
            
        #     res = False
        #     for j in range(1, nums[i] + 1):
        #         res = res or dfs(i + j)
            
        #     memo[i] = res
        #     return res
        
        # return dfs(0)

        memo = [False for _ in range(len(nums))]
        memo[len(nums) - 1] = True

        for i in range(len(nums) - 1, -1, -1):
            
            for j in range(1, nums[i] + 1):
                if j + i >= len(nums) - 1:
                    memo[i] = True
                else:
                    memo[i] = memo[i] or memo[i + j]
                
                if memo[i]:
                    break
        
        return memo[0]
                