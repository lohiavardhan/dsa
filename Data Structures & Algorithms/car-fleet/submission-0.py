class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        answer = []
        for i in range(len(position)):
            answer.append((target - position[i]) // speed[i])
        
        answer.sort()

        answer_set = set(answer)


        res = len(answer_set)


        return res