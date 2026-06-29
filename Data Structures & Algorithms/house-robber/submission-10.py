class Solution:
    def rob(self, nums: List[int]) -> int:
        
        answer = [-1 for _ in range(len(nums))]

        answer[-1] = nums[-1]
        answer[-2] = nums[-2]

        for i in range(len(nums) - 3, -1, -1):
            print(answer)
            answer[i] = max(nums[i] + answer[i + 2],  answer[i + 1])


        return max(answer[0], answer[1]) 