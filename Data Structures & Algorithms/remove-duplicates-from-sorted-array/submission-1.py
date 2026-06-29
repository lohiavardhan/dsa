class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i -1 >= 0 and nums[i - 1] == nums[i]:
                nums.pop(i)
                continue
            i += 1
        
        return len(nums)