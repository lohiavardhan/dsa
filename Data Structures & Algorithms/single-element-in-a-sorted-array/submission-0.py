class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        nums.sort()

        l = 0
        r = 1

        while True:
            if nums[l] != nums[r]:
                return nums[l]
            
            l += 2
            r += 2
        
        