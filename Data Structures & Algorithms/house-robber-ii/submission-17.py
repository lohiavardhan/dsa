class Solution:
    def rob(self, nums: List[int]) -> int:

        def hrob1(nums):
            if len(nums) <= 2:
                return max(nums)
            answer = [0 for i in nums]

            answer[0] = nums[0]
            answer[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                answer[i] = max(nums[i] + answer[i - 2], answer[i - 1])
                
            return answer[len(nums) - 1]
        
        if len(nums) <= 3:
            return max(nums)
        
        return max(hrob1(nums[1:]), hrob1(nums[:-1]))
        