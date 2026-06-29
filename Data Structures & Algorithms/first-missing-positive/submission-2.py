class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            index_to_mark = abs(nums[i]) - 1
            if index_to_mark >= len(nums) or nums[index_to_mark] < 0:
                continue
            if nums[index_to_mark] == 0:
                nums[index_to_mark] = float('-inf')
            else:
                nums[index_to_mark] = - nums[index_to_mark]
        
        print(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] >= 0:
                return i
        
        return i + 1
        # return 1