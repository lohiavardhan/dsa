class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        before = [None for i in range(len(nums))]
        after = [None for i in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                before[0] = nums[0]
            else:
                before[i] = before[i - 1] * nums[i]
        
        for i in range(len(nums) - 1, -1 , -1):
            if i == len(nums) - 1:
                after[len(nums) - 1] = nums[len(nums) - 1]
            else:
                after[i] = after[i + 1] * nums[i]

        print(before, after)

        res = [None for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                res[0] = after[0]
            elif i == len(nums) - 1:
                res[len(nums) - 1] = before[len(nums) - 2]
            else:
                res[i] = before[i-1] * after[i+1]
        
        print(res)


        return res
        