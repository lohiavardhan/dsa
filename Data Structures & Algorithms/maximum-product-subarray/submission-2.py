class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        dp = [i for i in nums]
        dp[len(nums) - 1] = nums[len(nums) - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if(dp[i] > nums[i] * nums[j]):
                    print(dp)
                    break
                else:
                    dp[i] = nums[i] * nums[j]
        
        
        return max(dp)