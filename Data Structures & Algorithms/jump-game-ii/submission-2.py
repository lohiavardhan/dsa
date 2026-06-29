class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [float('inf') for _ in range(len(nums))]
        dp[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= len(nums) - 1:
                dp[i] = 1
            else:
                for j in range(i, i + nums[i] + 1):
                    if j >= len(nums) - 1:
                        dp[i] = 1
                    else:
                        dp[i] = min(dp[i], 1 + dp[j]) 
            #print(i, dp)
                
        #print(dp)
        return dp[0]