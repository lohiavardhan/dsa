class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if len(gas) < len(cost):
            return -1

        tank = 0
        i = 0
        
        while i < len(gas):
            tank = gas[i] - cost[i]
            
            if tank < 0:
                i += 1
                continue
            
            j = i + 1
            j %= len(gas)
            res = True
            
            while j != i:
                
                tank += gas[j] - cost[j]
                
                if tank < 0:
                    res = False
                    break
                
                j += 1
                j %= len(gas)
            
            print(i, j)
            if res:
                return i
            else:
                if j > i:
                    i = j + 1
                else:
                    i += 1
        
        return -1