class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if len(gas) < len(cost):
            return -1

        tank = 0
        
        for i in range(len(gas)):
            tank = gas[i] - cost[i]
            if tank < 0:
                continue
            j = i + 1
            j %= len(gas)
            res = True
            while j != i:
                
                tank += gas[j] - cost[j]
                
                if tank < 0:
                    print(i, j)
                    res = False
                    break
                
                j += 1
                j %= len(gas)
            
            if res:
                return i
        
        return -1