class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, j):
            if i in memo:
                return memo[(i, j)]
            if i == len(nums):
                return 0
            
            res = dfs(i + 1, j)
            if nums[i] > nums[j] or j == -1:
                res = max(res, 1 + dfs(i + 1, i))
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, -1)