class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0

        stack = []

        for i in range(len(heights)):
            curr_height = heights[i]

            print(i, stack)

            if stack and curr_height > heights[stack[-1]]:
                area = heights[stack[-1]] * (len(stack) + 1)
                max_area = max(stack[0], max(stack), area)

                while len(stack) > 0:
                    stack.pop()
                
            stack.append(i)
        
        return max(max_area, heights[stack[0]])