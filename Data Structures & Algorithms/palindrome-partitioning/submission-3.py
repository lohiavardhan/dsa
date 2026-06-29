class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def ispalindrome(string):
            l = 0
            r = len(string) - 1

            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        res = []

        def backtrack(curr_list, start):
            if start == len(s):
                res.append(curr_list.copy())
                return
            
            for r in range(start, len(s)):
                if ispalindrome(s[start:r + 1]):
                    curr_list.append(s[start:r + 1])
                    backtrack(curr_list, r + 1)
                    curr_list.pop()

        backtrack([], 0)   
        return res