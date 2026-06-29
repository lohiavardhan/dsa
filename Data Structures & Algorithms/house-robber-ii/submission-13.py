class Solution:
    def rob(self, nums: List[int]) -> int:
        
        answer_list = [0 for _ in nums]
        
        length = len(nums)

        if length <= 3:
            return max(nums)
        
        if length == 4:
            return nums[0] + max(nums[1:4])

        answer_list[length - 1] = nums[length - 1]
        answer_list[length - 2] = nums[length - 2]
        answer_list[length - 3] = nums[length - 3]

        i = length - 4
        while i >= 0:
            answer_list[i] = max(answer_list[i + 3] + nums[i], answer_list[i + 2], answer_list[i + 1])
            i -= 1

        return answer_list[0]            