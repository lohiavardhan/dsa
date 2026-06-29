class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        max_area = 0

        for i in range(len(heights)):
            curr_height = heights[i]

            index = -1
            while stack and stack[-1][1] > curr_height:
                (index, height) = stack.pop()
                area = height * (i - index)
                max_area = max(area, max_area)
            
            if index != -1:
                stack.append((index, curr_height))
            else:
                stack.append((i, curr_height))
        
        print(stack)
        for (index, height) in stack:
            area = height * (stack[-1][0] - index + 1)
            max_area = max(area, max_area)
        
        return max_area
