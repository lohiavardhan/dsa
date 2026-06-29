class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = float('-inf')

        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                res = max(res, total)
        
        return res
