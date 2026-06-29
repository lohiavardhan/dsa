class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(sublist, open_cnt, close_cnt):
            if open_cnt == n and close_cnt == n:
                res.append("".join(sublist))
                return
            if close_cnt > open_cnt or open_cnt > n or close_cnt > n or len(sublist) > (n * 2):
                return
            
            sublist.append('(')
            dfs(sublist, open_cnt + 1, close_cnt)
            sublist.pop()
            sublist.append(')')
            dfs(sublist, open_cnt, close_cnt + 1)
            sublist.pop()
        
        dfs([], 0, 0)
        return res