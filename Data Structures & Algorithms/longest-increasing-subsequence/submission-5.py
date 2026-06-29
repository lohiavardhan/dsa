class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS = [1 for _ in nums]
        LIS[len(nums) - 1] = 1

        i = len(nums) - 2
        while i >= 0:
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

            i -= 1
        
        print(LIS)
        return max(LIS)

        return 0