class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        test_list = []

        def backtrack(i, j, subset):
            if(subset == word):
                test_list.append(1)
                
            
            if(j >= len(board)):
                return
            if(i >= len(board[0])):
                backtrack(0, j + 1, subset)
                return
                
            
            subset += board[j][i]
            backtrack(i + 1, j, subset)

            subset = subset[:-1]
            backtrack(i + 1, j, subset)

        backtrack(0, 0, "")

        if(len(test_list) >= 1):
            return True
        
        return False

