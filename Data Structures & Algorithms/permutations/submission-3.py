class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        
        def dfs(curr_set, curr_list):
            if len(curr_set) == len(nums):
                res.append(curr_list.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in curr_set:
                    curr_set.add(nums[i])
                    curr_list.append(nums[i])
                    dfs(curr_set, curr_list)
                    curr_set.remove(nums[i])
                    curr_list.pop()
                
        for i in range(len(nums)):
            sets = set()
            sets.add(nums[i])
            dfs(sets, [nums[i]])
        
        return res
