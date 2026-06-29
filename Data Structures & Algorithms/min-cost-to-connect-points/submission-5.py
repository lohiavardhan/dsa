class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for p1 in range(len(points)):
            for p2 in range(p1 + 1, len(points)):
                x1, y1, x2, y2 = points[p1][0], points[p1][1], points[p2][0], points[p2][1]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[p1].append((cost, p2))
                adj[p2].append((cost, p1))
        
        visited = set()
        cost = 0
        frontier = []
        heapq.heappush(frontier, (0, 0))

        while True:
            if len(visited) == len(points):
                return cost
            
            curr_cost, curr_point = heapq.heappop(frontier)
            if curr_point in visited:
                continue
            
            visited.add(curr_point)
            cost += curr_cost

            for next_cost, next_point in adj[curr_point]:
                if next_point in visited:
                    continue
                
                heapq.heappush(frontier, (next_cost, next_point))

        return -1
