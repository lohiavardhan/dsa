class Solution:
    def trap(self, height: List[int]) -> int:
        
        answer = 0
        i = 0

        print(height)

        while i < len(height):
            if i == 0 or i == len(height) - 1:
                i += 1
                continue
            
            l = max(height[0:i])
            r = max(height[i+1:])

            

            area = min(l, r) - height[i]

            print(f'{l=}, {r=}, {i=}, {height[i]=}, {area=}')

            if area > 0:
                answer += area
            i += 1
        
        return answer

            