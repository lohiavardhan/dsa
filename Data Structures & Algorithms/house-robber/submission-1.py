class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums) - 3, -1, -1):
            nums[i] += nums[i + 2]
        
        print(nums)
        return max(nums[0], nums[1])
        