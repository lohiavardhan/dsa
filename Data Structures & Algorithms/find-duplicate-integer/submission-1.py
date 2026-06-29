class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0, 1
        size = len(nums)

        while slow != fast:
            if nums[slow] == nums[fast]:
                return nums[slow]
            
            slow = (slow + 1) if (slow + 1) < len(nums) else 0
            fast = (fast + 2) if (fast + 2) < len(nums) else 0
        
        return -1

