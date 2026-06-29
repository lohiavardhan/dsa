class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        answer = [(0, 0) for _ in range(len(nums))]
        answer[0] = (nums[0], nums[0])
        print(answer)
        result = float("-inf")
        for i in range(1, len(nums)):
            maximum, minimum = answer[i - 1][0] , answer[i - 1][1]

            if nums[i] == 0:
                curr_max = 1
                curr_min = 1
            else:
                curr_max = max(nums[i], maximum * nums[i], minimum * nums[i])
                curr_min = min(nums[i], maximum * nums[i], minimum * nums[i])
                result = max(result, curr_max)

            answer[i] = (curr_max, curr_min)
        

        print(answer)
        return result