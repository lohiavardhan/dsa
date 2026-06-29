class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if(i >= len(nums)):
                return
            

            adder = 0
            for x in subset:
                adder += x
            if(adder == target):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)

        return []
        