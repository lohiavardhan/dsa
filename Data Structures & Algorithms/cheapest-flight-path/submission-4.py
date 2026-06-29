class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)
        for source, dest, cost in flights:
            adj[source].append((cost, dest))
        
        frontier = []
        heapq.heappush(frontier, (0, src, 0))

        while frontier:
            cost, airport, stops = heapq.heappop(frontier)
            if airport == dst:
                return cost
            if stops > k:
                continue
            
            for next_cost, next_airport in adj[airport]:
                heapq.heappush(frontier, (cost + next_cost, next_airport, stops + 1))



        return -1