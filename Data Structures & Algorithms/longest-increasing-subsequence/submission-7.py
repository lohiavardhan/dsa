class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = {}
        
        def dfs(i, j):
            #print(dp)
            if i == len(nums):
                return 0
            if i in dp and nums[j] < nums[i]:
                return dp[i]
            
            
            res = dfs(i + 1, j)

            if j == -1 or nums[j] < nums[i]:
                res = max(res, 1 + dfs(i + 1, i))
            
            dp[i] = res
            return res
        
        print(dp)
        return dfs(0, -1)