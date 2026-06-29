class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0
        stack = []

        for i in range(len(heights)):
            curr_height = heights[i]
            index_popped = -1
            while stack and curr_height < stack[-1][1]:
                (index_popped, height_popped) = stack.pop()
                area_contri = (i - index_popped) * height_popped
                max_area = max(max_area, area_contri)

            if index_popped == -1:
                stack.append((i, heights[i]))
            else:
                stack.append((index_popped, heights[i]))

        print(stack)
        

        while stack:
            (index_popped, height_popped) = stack.pop()
            area_contri = (len(heights) - index_popped) * height_popped
            print(index_popped, height_popped, len(heights) - 1, area_contri, max_area)
            max_area = max(max_area, area_contri)
        
        print(max_area)
        
        return max_area