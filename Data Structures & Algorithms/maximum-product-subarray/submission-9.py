class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_sub = 0
        min_sub = 0

        for num in nums:
            max_sub = max(num, num * min_sub, num * max_sub)
            min_sub = min(num, num * min_sub, num * max_sub)

        return max_sub
