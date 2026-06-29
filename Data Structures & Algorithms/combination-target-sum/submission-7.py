class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, subarray, total):
            if total == target:
                res.append(subarray.copy())
                return
            if total > target or i >= len(nums):
                return 
            
            subarray.append(nums[i])
            dfs(i, subarray, total + nums[i])
            subarray.pop()
            dfs(i + 1, subarray, total)
        
        dfs(0, [], 0)
        return res