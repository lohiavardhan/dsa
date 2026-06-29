class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        answer = 0
        visited = set()
        def dfs(i, j):
            nonlocal answer
            if sum(nums[i:j + 1]) > k or i > j or j >= len(nums):   
                return False
            if sum(nums[i:j + 1]) == k:
                if (i, j) not in visited:
                    answer += 1
                visited.add((i, j))
            
            
            dfs(i, j + 1)
            dfs(i + 1, j)
        
        for i in range(len(nums)):
            dfs(i, i)

        return answer
            
