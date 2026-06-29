class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #if len(nums) == 1:
            #return nums[0]
        
        res = 0
        total = float('-inf')

        for num in nums:
            if total != float('-inf') and total + num < 0:
                res = 0
                total = float('-inf')
            else:
                res += 1
                total = total + num if total != float('-inf') else num
        
        return total
