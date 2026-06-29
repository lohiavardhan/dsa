class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
    
    def helper(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) < 2:
            return nums[0]
        
        answer = [-1 for _ in range(len(nums) + 1)]
        answer[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            answer[i] = max(nums[i] + answer[i + 2], answer[i + 1])
        
        print(answer)
        return answer[0]
        
