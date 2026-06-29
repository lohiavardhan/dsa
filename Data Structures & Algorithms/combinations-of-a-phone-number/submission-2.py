class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        def backtrack(i, curr_list):
            if i == len(digits):
                res.append("".join(curr_list))
                return
            
            for char in mapping[digits[i]]:
                curr_list.append(char)
                backtrack(i + 1, curr_list)
                curr_list.pop()

        backtrack(0, [])  
        return res
