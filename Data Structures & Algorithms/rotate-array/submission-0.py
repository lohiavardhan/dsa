class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = k - 1
        r = len(nums) - 1

        while l >= 0:
            nums[l], nums[r] = nums[r], nums[l]
            l -= 1
            r -= 1
        
