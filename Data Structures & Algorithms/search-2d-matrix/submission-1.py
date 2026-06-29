import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if matrix[i][-1] < target or matrix[i][0] > target:
                continue
            
            l = 0
            r = len(matrix[0]) - 1

            while l < r:
                mid = (l + r) // 2

                if matrix[i][mid] == target:
                    return True

                if matrix[i][l] < matrix[i][mid]:
                    l = mid + 1
                else:
                    r = mid - 1






        return False