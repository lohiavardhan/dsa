class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = collections.deque()
        answer = [0 for i in range(len(temperatures))]

        for r in range(len(temperatures)):
            while stack and temperatures[r] > temperatures[stack[-1]]:
                answer[stack[-1]] = r - stack[-1]
                stack.pop()
            
            stack.append(r)
        

        return answer
