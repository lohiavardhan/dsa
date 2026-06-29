class Solution:
    def rob(self, nums: List[int]) -> int:

        length = len(nums)

        answer_array = [0 for _ in nums]

        answer_array[length - 1] = nums[length - 1]
        answer_array[length - 2] = nums[length - 2]

        i = length - 3

        while i >= 0:
            answer_array[i] = max(nums[i] + answer_array[i + 2], answer_array[i + 1])
            i -= 1
        
        return answer_array[0]
        