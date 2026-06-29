class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set(nums)
        for i in range(min(nums), max(nums)):
            if i not in hashset:
                return i
        
        return i + 2