class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for asteroid in asteroids:
            print(stack)
            remaining = asteroid
            while stack and ((stack[-1] > 0 and remaining < 0) or (stack[-1] < 0 and remaining > 0)):
                rock = stack.pop()
                if abs(rock) == abs(remaining):
                    remaining = 0
                else:
                    if abs(rock) > abs(remaining):
                        remaining = rock
                    else:
                        remaining = remaining
            
            if remaining > 0:
                stack.append(remaining)
        
        return stack

