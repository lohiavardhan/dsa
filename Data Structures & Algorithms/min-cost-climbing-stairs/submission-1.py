class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) == 1:
            return cost[0]

        if len(cost) == 2:
            return min(cost[0], cost[1])

        if len(cost) == 3:
            return min(cost[0] + cost[2], cost[1])
        
        cost_to_reach_goal = [0] * (len(cost))
        cost_to_reach_goal[len(cost) - 1] = cost[len(cost) - 1]
        cost_to_reach_goal[len(cost) - 2] = cost[len(cost) - 2]

        i = len(cost) - 3
        while i >= 0:
            cost_to_reach_goal[i] = min(cost[i] + cost_to_reach_goal[i + 1], cost[i] + cost_to_reach_goal[i + 2])
            i -= 1

        print(cost_to_reach_goal)
        return min(cost_to_reach_goal[0], cost_to_reach_goal[1])
        
        