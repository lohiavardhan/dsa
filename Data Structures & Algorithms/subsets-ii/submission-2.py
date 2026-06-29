class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result_list = []
        nums.sort()

        def dfs(curr_list, i):
            if i >= len(nums):
                result_list.append(curr_list.copy())
                return
            
            curr_list.append(nums[i])
            dfs(curr_list, i + 1)

            curr_list.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(curr_list, i + 1)
        
        dfs([], 0)

        return result_list
        