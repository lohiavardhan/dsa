class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [float('inf') for _ in range(len(nums))]
        dp[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= len(nums) - 1:
                dp[i] = 1
            else:
                for j in range(1, i + nums[i] + 1):
                    #print(i, j, dp)
                    if i + j >= len(nums) - 1:
                        dp[i] = 1
                    else:
                        dp[i] = min(dp[i], 1 + dp[i + j]) 
                
        #print(dp)
        return dp[0]