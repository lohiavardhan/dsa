class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse(num):
            l = 0
            r = len(num) - 1

            while l < r:
                num[l], num[r] = num[r], num[l]
                l += 1
                r -= 1
            
            return num
        
        nums = reverse(nums)
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])
            