class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(string):
            l = 0
            r = len(string) - 1

            while l <= r:
                if string[l] != string[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True

        
        def dfs(curr_arr, i):
            if i == len(s):
                res.append(curr_arr.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s[i: j + 1]):
                    curr_arr.append(s[i:j + 1])
                    dfs(curr_arr, j + 1)
                    curr_arr.pop()
        
        dfs([], 0)

        return res