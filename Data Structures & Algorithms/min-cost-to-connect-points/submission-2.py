class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        visited = set()
        frontier = []
        res_cost = defaultdict(int)

        adj = defaultdict(list)

        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                cost = abs(x2 - x1) + abs(y2 - y1)
                adj[(x1, y1)].append((cost, x2, y2))
        
        heapq.heappush(frontier, (0, points[0][0], points[0][1]))

        while len(visited) < len(points):
            curr_cost, x1, y1 = heapq.heappop(frontier)
            if (x1, y1) in visited:
                continue
            print(res_cost)
            res_cost[(x1, y1)] = curr_cost
            visited.add((x1, y1))

            for next_cost, x2, y2 in adj[(x1, y1)]:
                if (x2, y2) in visited:
                    continue
                
                heapq.heappush(frontier, (next_cost, x2, y2))
        
        print(sum(res_cost.values()))
            



        return sum(res_cost.values())
