class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        answer_list = []
        candidates.sort()

        def dfs(i, curr_sum, curr_list):
            if curr_sum == target:
                answer_list.append(curr_list.copy())
                return
            
            if curr_sum > target or i >= len(candidates):
                return
            
            curr_list.append(candidates[i])
            dfs(i + 1, curr_sum + candidates[i], curr_list)

            curr_list.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, curr_sum, curr_list)
        
        dfs(0, 0, [])
        return answer_list