class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        dp = {}

        if sum(nums) % 2 != 0:
            return False

        def dfs(target, i):
            if (target, i) in dp:
                return dp[(target, i)]
            if i >= len(nums):
                return False
            if nums[i] == target:
                return True
            
            res = dfs(target, i + 1) or dfs(target - nums[i], i + 1)
            dp[(target, i)] = res
            return res
        
        return dfs(sum(nums) / 2, 0)