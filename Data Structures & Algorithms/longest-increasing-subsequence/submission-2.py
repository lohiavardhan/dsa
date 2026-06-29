class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        curr_max = 0
        def isincreasing(array):
            return all(array[i] < array[i + 1] for i in range(len(array) - 1))

        def dfs(i, curr_list):
            nonlocal curr_max
            if i == len(nums):
                if isincreasing(curr_list):
                    curr_max = max(curr_max, len(curr_list))
                return
            
            
            
            curr_list.append(nums[i])
            dfs(i + 1, curr_list)

            curr_list.pop()
            dfs(i + 1, curr_list)
        
        dfs(0, [])
        return curr_max