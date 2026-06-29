class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        max_sub, min_sub = 1, 1

        for i in range(0, len(nums)):
            max_sub = max(nums[i], nums[i] * min_sub, nums[i] * max_sub)
            min_sub = min(nums[i], nums[i] * min_sub, nums[i] * max_sub)
            res = max(res, max_sub)

        return res
