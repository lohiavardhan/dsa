class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    #print(f'{i=}, {j=}, {nums[i]=}, {nums[j]=}, {dp=}')
        
        #print(dp)
        return max(dp)