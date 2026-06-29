class Solution:
    
    
    def rob(self, nums: List[int]) -> int:
        

        def helper(array):
            if len(nums) == 1:
                return nums[0]
            
            if len(nums) == 2:
                return max(nums[0], nums[1])
            
            num1, num2 = 0, 0

            for i in range(len(array)):
                temp = max(array[i] + num1, num2)
                num1 = num2
                num2 = temp
            
            return num2


        result1 = helper(nums[:-1])
        result2 = helper(nums[1:])
        return max(result1, result2)

    
            