class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitstochar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def dfs(i, currstring):
            if(len(currstring) >= len(digits)):
                res.append(currstring)
                return

            for c in digitstochar[digits[i]]:
                dfs(i + 1, currstring + c)

        if digits:
            dfs(0, "")
        
        return res


        
        