class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        
        pos_speed.sort(reverse=True)
        s = []
        res = 0

        for i in range(len(pos_speed)):
            pos = pos_speed[i][0]
            spd = pos_speed[i][1]
            time = (target - pos) / spd
            
            if not s:
                s.append(time)
            else:
                if time > s[-1]:
                    res += 1
                    while s:
                        s.pop()
                    s.append(time)
                else:
                    s.append(s[-1])
        

        return res + 1 if s else res
            