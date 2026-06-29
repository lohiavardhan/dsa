class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        level_left = 0
        level_right = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        

        while(level_left <= level_right):
            mid_level = (level_left + level_right) // 2
            
            if(matrix[mid_level][-1] < target):
                level_left = mid_level + 1
            elif(matrix[mid_level][0] > target):
                level_right = mid_level - 1
            else:
                break
        
        while(left <= right):
                mid = (left + right) // 2
                

                if(matrix[mid_level][mid] < target):
                    left = mid + 1
                elif(matrix[mid_level][mid] > target):
                    right = mid - 1
                else:
                    return True
        
        
        return False