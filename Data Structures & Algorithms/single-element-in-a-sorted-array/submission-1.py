class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        nums.sort()

        i = 0

        while True:
            if i >= len(nums) - 1 or nums[i] != nums[i + 1]:
                return nums[i]
            i += 2 
        
