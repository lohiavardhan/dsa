class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}
        
        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            res = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            memo[(i, total)] = res

            return res
        
        return dfs(0, 0)
            