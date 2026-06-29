class Solution:
    def checkValidString(self, s: str) -> bool:
        
        left_idx = []
        star_idx = []

        for i, char in enumerate(s):
            if char == '(':
                left_idx.append(i)
            elif char == ')':
                if len(left_idx) == 0:
                    if len(star_idx) == 0:
                        return False
                    else:
                        star_idx.pop()
                else:
                    left_idx.pop() 
            else:
                star_idx.append(i)
        
        for i in range(len(star_idx) - 1, -1, -1):
            if left_idx and star_idx[i] > left_idx[-1]:
                left_idx.pop()
        
        return len(left_idx) == 0
        
