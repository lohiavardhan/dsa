class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        LIS = [1] * len(nums)

        i = len(nums) - 1

        while(i >= 0):
            for j in range(i, len(nums)):
                if(nums[i] < nums[j]):
                    LIS[i] = max(LIS[i], 1 + LIS[j])

            i -= 1
        return max(LIS)
