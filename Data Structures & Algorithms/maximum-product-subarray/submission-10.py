class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_sub = 1
        min_sub = 1

        for num in nums:
            
            max_sub = max(num, num * min_sub, num * max_sub)
            min_sub = min(num, num * min_sub, num * max_sub)

        return max_sub
