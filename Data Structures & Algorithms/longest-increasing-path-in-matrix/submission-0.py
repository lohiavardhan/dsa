class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        coordinates = [[0 , 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(i, j):
            res = 1
            for coordinate in coordinates:
                new_i, new_j = i + coordinate[0], j + coordinate[1]
                if new_i < len(matrix) and new_j < len(matrix[0]) and new_i >= 0 and new_j >= 0 and matrix[new_i][new_j] > matrix[i][j]:
                    res = max(res, 1 + dfs(new_i, new_j))
            
            return res
        
        return max(dfs(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])))
