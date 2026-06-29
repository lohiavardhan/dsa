class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, prev_num):
            if (i, prev_num) in memo:
                return memo[(i, prev_num)]
            if i == len(nums):
                return 0
            
            res = dfs(i + 1, prev_num)
            if nums[i] > prev_num:
                res = max(res, 1 + dfs(i + 1, nums[i]))
            
            memo[(i, prev_num)] = res
            return res
        
        return dfs(0, float('-inf'))