class Solution:
    def rob(self, nums: List[int]) -> int:

        amount_stolen = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        amount_stolen[-1] = nums[-1]
        amount_stolen[-2] = nums[-2]
        amount_stolen[-3] = nums[-3] + amount_stolen[-1]

        for i in range(len(nums) - 4, -1, -1):
            amount_stolen[i] = max(nums[i] + amount_stolen[i + 2], nums[i] + amount_stolen[i + 3])


        print(amount_stolen)
        return max(amount_stolen[0], amount_stolen[1])
        