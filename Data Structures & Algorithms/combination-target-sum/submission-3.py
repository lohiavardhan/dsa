class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        answer_list = []

        def dfs(curr_list, curr_sum, index):
            if curr_sum == target:
                answer_list.append(curr_list.copy())
                return
            
            if curr_sum > target or index >= len(nums):
                return
            
            curr_list.append(nums[index])
            dfs(curr_list, curr_sum + nums[index], index)

            curr_list.pop()
            dfs(curr_list, curr_sum, index + 1)


        dfs([], 0, 0)
        
        return answer_list