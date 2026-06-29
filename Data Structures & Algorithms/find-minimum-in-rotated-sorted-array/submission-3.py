class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        minimum = nums[0]


        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            print(mid)
            minimum = min(nums[mid], minimum)
            
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            
        return minimum