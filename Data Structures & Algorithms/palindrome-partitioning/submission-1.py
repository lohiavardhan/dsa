class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def pali(string):
            return string == string[::-1]

        def dfs(i, curr_parts):
            if i >= len(s):
                res.append(curr_parts.copy())
                return
            
            for j in range(i, len(s)):
                if pali(s[i:j+1]):
                    curr_parts.append(s[i:j+1])
                    dfs(j + 1, curr_parts)
                    curr_parts.pop()

        dfs(0, [])

        return res


        return res
        