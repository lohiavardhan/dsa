class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        translation = {'2': 'abc',
         '3': 'def',
         '4': 'ghi',
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz'}

        answer = []

        def dfs(i, string):
            if(i >= len(digits)):
                answer.append(string)
                return

            curr_string = translation[digits[i]]

            for s in curr_string:
                dfs(i + 1, string + s)
        
        dfs(0, '')
        if digits == "":
            return []
        return answer
