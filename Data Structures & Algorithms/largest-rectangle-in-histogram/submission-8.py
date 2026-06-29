class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        answer = 0

        for i in range(len(heights)):
            popped_idx = -1
            while len(stack) > 0 and heights[i] < stack[-1][1]:
                popped_idx, popped_height  = stack.pop()
                answer = max(answer, (i - popped_idx) * popped_height)
            
            print(f'{popped_idx=}, {i=}, {heights[i]=}, {stack=}')
            if popped_idx != -1:
                stack.append([popped_idx, heights[i]])
            else:
                stack.append([i, heights[i]])
            
            print(f'{popped_idx=}, {i=}, {heights[i]=}, {stack=}')

        while stack:
            popped_idx, popped_height  = stack.pop()
            answer = max(answer, (len(heights) - popped_idx) * popped_height)
        
        return answer