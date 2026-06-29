class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        mid = 0
        while mid <= r:
            print(f'{l=}, {r=}, {mid=}, {nums[mid]}, {nums}')
            if nums[mid] == 0:
                nums[mid], nums[l] = nums[l], nums[mid] 
                l += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1
            else:
                mid += 1
        return nums