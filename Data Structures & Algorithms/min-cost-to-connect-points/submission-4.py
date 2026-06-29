class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for p1 in range(len(points)):
            for p2 in range(p1 + 1, len(points)):
                
                x1, y1 = points[p1]
                x2, y2 = points[p2]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[p1].append((cost, p2))
                adj[p2].append((cost, p1))
        
        res = 0
        frontier = []
        heapq.heappush(frontier, (0, 0))
        visited = set()

        while len(visited) < len(points):
            cost, p = heapq.heappop(frontier)
            if p in visited:
                continue
            visited.add(p)
            res += cost

            for next_cost, next_p in adj[p]:
                if next_p in visited:
                    continue
                heapq.heappush(frontier, (next_cost, next_p))
        
        return res