class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 3:
            return max(nums)
        
        answer_first = [-1 for i in range(len(nums))]
        answer_last = [-1 for i in range(len(nums))]

        answer_first[-2] = nums[-2]
        answer_first[-3] = nums[-3]

        answer_last[-1] = nums[-1]
        answer_last[-2] = nums[-2]

        for i in range(len(nums) - 3, -1, -1):
            if i == len(nums) - 3:
                answer_first[i] = max(answer_first[i + 1], nums[i])
            else:
                answer_first[i] = max(answer_first[i + 1], nums[i] + answer_first[i + 2])
        
        for i in range(len(nums) - 2, 0, -1):
            if i + 2 < len(nums):
                answer_last[i] = max(answer_last[i + 1], nums[i] + answer_last[i + 2])
            else:
                answer_last[i] = max(answer_last[i + 1], nums[i])
        
        print(answer_first, answer_last)
        return max(answer_first[0], answer_first[1], answer_last[1], answer_last[2])

        return 0
        
        