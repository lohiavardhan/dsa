class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = k - 1
        r = len(nums) - 1
        print(nums)
        while l >= 0:
            print(l, r, nums[l], nums[r])
            nums[l], nums[r] = nums[r], nums[l]
            l -= 1
            r -= 1
        
        nums[k:] = nums[len(nums) - k:] + nums[k: len(nums) - k]
        # while r > k - 1:
            