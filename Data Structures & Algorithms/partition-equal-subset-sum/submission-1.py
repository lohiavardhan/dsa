class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def dfs(part1, part2, i):
            if i == len(nums):
                if part1 == part2:
                    return True
                else:
                    return False
            
            return dfs(part1 + nums[i], part2, i + 1) or dfs(part1, part2 + nums[i], i + 1)
        
        return dfs(0, 0, 0)