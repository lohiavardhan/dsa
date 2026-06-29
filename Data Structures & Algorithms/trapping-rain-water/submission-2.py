class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1

        leftMax = float('-infinity')
        rightMax = float('-infinity')


        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
            # leftMax = max(leftMax, height[l])
            # rightMax = max(rightMax, height[r])
            
            # curr_amount = min(leftMax, rightMax)
            
            # res += max(0, curr_amount - height[l])

            # print(f'{l=}, {leftMax=}, {rightMax=}, {curr_amount=}, {height[l]=}, {res=}')

            # l += 1
            # r += 1
        
        return res