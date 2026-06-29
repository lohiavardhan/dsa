class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        curr = nums[0]
        i = 0
        while True:
            if i >= len(nums) - 1:
                return True
            
            if nums[i] == 0:
                return False
            
            i += nums[i]