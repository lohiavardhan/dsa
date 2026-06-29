class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        answer_list =  [-math.inf for _ in nums]
        
        answer_list[len(nums) - 1] = nums[len(nums) - 1]

        i = len(nums) - 2
        prev_used = False
        while i >= 0:
            curr_max = max(nums[i] * answer_list[i + 1], nums[i], answer_list[i + 1], nums[i] * nums[i + 1])
            if prev_used:
                curr_max = max(nums[i], answer_list[i + 1], nums[i] * nums[i + 1])
                prev_used = False
            
            if curr_max == answer_list[i + 1]:
                prev_used = True

            answer_list[i] = curr_max
            i -= 1
            print(answer_list)
        
        return answer_list[0]
