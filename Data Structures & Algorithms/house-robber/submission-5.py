class Solution:
    def rob(self, nums: List[int]) -> int:
        
        

        def backtrack(i, curr_sum):
            if i >= len(nums):
                return curr_sum
            
            answer = max(backtrack(i + 2, curr_sum + nums[i]), backtrack(i + 1, curr_sum))

            return answer
        
        return backtrack(0, 0)
            