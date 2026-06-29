class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        dp = {}

        def dfs(part1, part2, i):
            if (part1, part2, i) in dp:
                return dp[(part1, part2, i)]
            if i == len(nums):
                if part1 == part2:
                    return True
                else:
                    return False
            
            res = dfs(part1 + nums[i], part2, i + 1) or dfs(part1, part2 + nums[i], i + 1)
            dp[(part1, part2, i)] = res
            return res
        
        return dfs(0, 0, 0)