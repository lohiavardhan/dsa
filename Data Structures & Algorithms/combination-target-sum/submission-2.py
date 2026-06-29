class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def dfs(curr_list, curr_sum, i):
            if curr_sum == target:
                result.append(curr_list.copy())
                return
            
            if i >= len(nums) or curr_sum > target:
                return
            
            curr_list.append(nums[i])
            dfs(curr_list, curr_sum + nums[i], i)

            curr_list.pop()
            dfs(curr_list, curr_sum, i + 1)
        
        dfs([], 0, 0)

        return result