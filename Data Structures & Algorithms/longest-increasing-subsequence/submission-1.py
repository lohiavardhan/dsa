class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        answer_array = [0 for num in nums]
        answer_array[0] = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                answer_array[i] = answer_array[i - 1] + 1
            else:
                answer_array[i] = answer_array[i - 1]
        
        return answer_array[len(nums) - 1]
        