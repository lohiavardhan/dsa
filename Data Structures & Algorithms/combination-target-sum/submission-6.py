class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        answer = []

        def backtrack(curr_arr, i):
            if sum(curr_arr) > target:
                return
            if sum(curr_arr) == target:
                answer.append(curr_arr.copy())
                return
            
            
            for j in range(i, len(nums)):
                curr_arr.append(nums[j])
                backtrack(curr_arr, j)
                curr_arr.pop()
                # backtrack(curr_arr)
        
        backtrack([], 0)

        return answer