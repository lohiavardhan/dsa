import os
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        convert = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        def dfs(i, curr_arr):
            if i == len(digits):
                res.append("".join(curr_arr.copy()))
                return
            
            for digit in convert[digits[i]]:
                curr_arr.append(digit)
                dfs(i + 1, curr_arr)
                curr_arr.pop()
            
        dfs(0, [])

        return res if digits else []