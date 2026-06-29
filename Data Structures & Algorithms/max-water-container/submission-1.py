class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        answer = 0

        prev = 1

        while l < r:
            answer = max(answer, min(heights[l], heights[r]) * (r - l))
            if prev == 1:
                l += 1
                prev = 0
            else:
                r -= 1
                prev = 1
            
            

        
        return answer
            
        