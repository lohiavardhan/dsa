class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []

        subset = []
    
        def dfs(i):
            if(i >= len(nums)):
                test = subset.copy()
                test.sort()
                if (test not in res):
                    res.append(test.copy())
                return
            

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
        