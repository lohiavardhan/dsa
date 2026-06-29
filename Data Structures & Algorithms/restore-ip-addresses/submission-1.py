class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []

        def isValid(string):
            if len(string) >= 2 and string[0] == '0':
                return False
            return 0 <= int(string) <= 255

        def dfs(i, curr_arr):
            if i == len(s) and len(curr_arr) == 4:
                res.append(".".join(curr_arr))
                return
            
            for j in range(i, len(s)):
                curr_str = s[i: j + 1]

                if isValid(curr_str):
                    curr_arr.append(curr_str)
                    dfs(j + 1, curr_arr)
                    curr_arr.pop()
        
        dfs(0, [])
        return res

