class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(visited):
            if tuple(visited) in memo:
                return memo[tuple(visited)]
            if len(visited) == len(nums):
                return 0
            
            res = 1

            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                left = i - 1
                
                while left in visited:
                    left = left - 1
                
                if left < 0:
                    left = -1
                
                right = i + 1
                while right in visited:
                    right = right + 1
                
                if right >= len(nums):
                    right = -1
                

                left_num = nums[left] if left != -1 else 1
                right_num = nums[right] if right != -1 else 1

                res = max(res, nums[i] * left_num * right_num + dfs(visited))

                visited.remove(i)
            
            memo[tuple(visited)] = res
            return res
        
        return dfs(set())