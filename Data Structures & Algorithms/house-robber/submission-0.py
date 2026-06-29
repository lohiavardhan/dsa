class Solution:
    def rob(self, nums: List[int]) -> int:

        for i in range(len(nums) - 3, -1, -1):
            nums[i] += nums[i + 2]
        
        print(nums)
        return max(nums[0], nums[1])
        