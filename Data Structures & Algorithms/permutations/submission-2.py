class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(curr, used):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    curr.append(nums[i])
                    used[i] = True
                    dfs(curr, used)
                    curr.pop()
                    used[i] = False
        
        used = [False] * len(nums)
        dfs([], used)
        return res