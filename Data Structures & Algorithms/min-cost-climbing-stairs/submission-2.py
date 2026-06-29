class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) < 2:
            return min(cost)
        
        answer = [-1 for _ in range(len(cost))]
        answer[-1] = cost[-1]
        answer[-2] = cost[-2]

        print(answer)

        for i in range(len(cost) - 3, -1, -1):
            answer[i] = cost[i] + min(answer[i + 1], answer[i + 2])
        

        return min(answer[0], answer[1])