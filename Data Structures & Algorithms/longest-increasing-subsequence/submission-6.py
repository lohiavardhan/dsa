class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1 for _ in range(len(nums))]
        max_idx = len(nums) - 1
        min_idx = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < nums[min_idx]:
                dp[i] = dp[min_idx] + 1
                min_idx = i
            
            
        return max(dp)

