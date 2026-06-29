class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        answer = []

        hashmap = {}

        for i in range(len(position)):
            hashmap[position[i]] = speed[i]
        
        hashmap = dict(sorted(hashmap.items(), reverse=True))

        print(hashmap)
        
        for (position,speed) in hashmap.items():
            time = (target - position) / speed
            answer.append(time)
        
        print(answer)
        
        for i in range(len(answer)):
            if i < len(answer) - 1 and answer[i] > answer[i + 1]:
                answer[i + 1] = answer[i]
        
        print(answer)

        answer_set = set(answer)


        res = len(answer_set)


        return res