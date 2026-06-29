class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        answer_list = []

        def dfs(i, curr_list):
            if i >= len(nums):
                answer_list.append(curr_list.copy())
                return

            curr_list.append(nums[i])
            dfs(i + 1, curr_list)

            curr_list.pop()
            dfs(i + 1, curr_list)
        
        dfs(0, [])

        return answer_list
        