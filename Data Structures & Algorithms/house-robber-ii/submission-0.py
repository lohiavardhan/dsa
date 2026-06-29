class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        if len(nums) == 3:
            return max(nums[0], nums[1])
        checker = 0
        nums[-3] += nums[-1]

        for i in range(len(nums) - 4, -1, -1):
            if nums[i + 2] > nums[i + 3]:
                if i + 2 == len(nums) - 1:
                    checker = 1
                nums[i] += nums[i + 2]
            
            else:
                if i + 3 == len(nums) - 1:
                    checker = 1
                nums[i] += nums[i + 3]
        
        print(checker, nums)
        if(checker == 1):
            return nums[1]
        return max(nums[0], nums[1])