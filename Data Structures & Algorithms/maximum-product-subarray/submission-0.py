class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        dp = [-1000000] * len(nums)
        dp[len(nums) - 1] = nums[len(nums) - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            #for j in range(i + 1, len(nums)):
            dp[i] = max(dp[i], nums[i] * nums[i + 1])
        

        return max(dp)