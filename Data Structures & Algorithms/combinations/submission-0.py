class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        answer_list = []

        def dfs(curr_list, curr_length, curr_num):
            if curr_length == k:
                answer_list.append(curr_list.copy())
                return
            
            if curr_num > n:
                return
            
            curr_list.append(curr_num)
            dfs(curr_list, curr_length + 1, curr_num + 1)

            curr_list.pop()
            dfs(curr_list, curr_length, curr_num + 1)

        dfs([], 0, 1)
        return answer_list
            
        