class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer_list = []

        def dfs(curr_sum, curr_list, i):
            if curr_sum == target:
                answer_list.append(curr_list.copy())
                return
            
            if (i >= len(nums)) or (curr_sum > target):
                return

            curr_list.append(nums[i])
            dfs(curr_sum + nums[i], curr_list, i)

            curr_list.pop()
            dfs(curr_sum, curr_list, i + 1)

        dfs(0, [], 0)
        return answer_list