class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        answer = []
        for i in range(len(position)):
            answer.append((target - position[i]) // speed[i])
        
        print(answer)
        
        for i in range(len(answer)):
            if i < len(answer) - 1 and answer[i] > answer[i + 1]:
                answer[i + 1] == answer[i]
        
        print(answer)

        answer_set = set(answer)


        res = len(answer_set)


        return res