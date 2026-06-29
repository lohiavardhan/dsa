class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        
        def backtrack(count_open, count_closed, curr):
            if count_open == n and count_closed == n:
                res.append("".join(curr))
                return
            
            if count_open > n or count_closed > n or count_closed > count_open:
                return
            
            curr.append('(')
            backtrack(count_open + 1, count_closed, curr)
            curr.pop()
            curr.append(')')
            backtrack(count_open, count_closed + 1, curr)
            curr.pop()
        
        backtrack(0, 0, [])

        return res