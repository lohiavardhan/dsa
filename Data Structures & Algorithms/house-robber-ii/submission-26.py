class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
    
    def helper(self, nums):

        
        answer = [-1 for _ in range(len(nums))]
        answer[-1] = nums[-1]
        answer[-2] = max(nums[-1], nums[-2])

        for i in range(len(nums) - 3, -1, -1):
            answer[i] = max(nums[i] + answer[i + 2], answer[i + 1])
        
        print(answer)
        return answer[0]
        
