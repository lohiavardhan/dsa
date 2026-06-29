class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        def dfs(i, sublist):
            if i == len(nums):
                res.append(sublist.copy())
                return
            
            sublist.append(nums[i])
            dfs(i + 1, sublist)
            sublist.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1, sublist)
        
        dfs(0, [])
        return res