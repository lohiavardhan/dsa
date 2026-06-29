class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        two = nums[len(nums) - 1]
        one = nums[len(nums) - 2]

        i = len(nums) - 3

        curr_max = 0

        while i >= 0:
            print(one, two, nums[i])
            curr_max = max(nums[i] + two, one)
            one, two = curr_max, one
            i -= 1
        
        return one