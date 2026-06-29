class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set(nums)
        i = 1
        while i <= max(nums):
            if i not in hashset:
                return i
            i += 1
        
        return i