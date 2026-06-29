class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s):
                while j < len(p):
                    if p[j] != '*':
                        return False
                    j += 2
                return True
            if j == len(p) and i != len(s):
                return False
            
            res = False
            
            if p[j] == '*':
                res = dfs(i, j + 1) or (i < len(s) and (s[i] == p[j-1] or p[j-1] == '.') and dfs(i + 1, j))
            elif s[i] == p[j] or p[j] == '.':
                res = dfs(i + 1, j + 1)
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)