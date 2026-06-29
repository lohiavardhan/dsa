class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}

        def dfs(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left > right:
                return 0
            
            res = 1

            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                coins += dfs(left, i - 1) + dfs(i + 1, right)
                res = max(res, coins)
            
            memo[(left, right)] = res
            return res
        
        return dfs(1, len(nums) - 2)