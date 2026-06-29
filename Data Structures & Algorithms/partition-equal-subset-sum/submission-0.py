class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums) % 2 != 0):
            return False
        
        list_check = []
        def dfs(i, subset1, subset2):
            if(i >= len(nums)):
                if(sum(subset1) == sum(subset2)):
                    list_check.append(subset1)

                return
            
            subset1.append(nums[i])
            dfs(i + 1, subset1, subset2)
            subset1.pop()
            subset2.append(nums[i])
            dfs(i + 1, subset1, subset2)
            subset2.pop()
        
        dfs(0, [], [])
        if(len(list_check) > 0):
            return True
        
        return False

