class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]

        answer = [0 for _ in range(len(nums))]
        answer[-1] = nums[-1]
        answer[-2] = nums[-2]

        for i in range(len(nums) - 3, -1, -1):
            answer[i] = max(answer[i + 1], nums[i] + answer[i + 2])
        
        return max(answer[0], answer[1])



        return 0