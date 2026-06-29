class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        def dfs(i, curr_list):
            if i == len(nums):
                res.append(curr_list.copy())
                return
            
            curr_list.append(nums[i])
            dfs(i + 1, curr_list)

            curr_list.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1, curr_list)
        
        dfs(0, [])

        return res