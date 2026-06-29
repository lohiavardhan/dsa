class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        while True:
            if heights[l + 1] > heights[l]:
                l += 1
                continue
            
            if heights[r - 1] > heights[r]:
                r -= 1
                continue
            
            return min(heights[l], heights[r]) * (r - l)
            
        