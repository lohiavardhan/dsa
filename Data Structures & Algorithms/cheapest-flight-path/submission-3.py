class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)

        for source, dest, price in flights:
            adj[source].append((price, dest))
        
        frontier = []
        heapq.heappush(frontier, (0, src, 0))
        while frontier:
            print(frontier)
            cost, airport, stops = heapq.heappop(frontier)
            print(cost, airport, dst, stops)
            if airport == dst and stops > 0:
                return cost
            if stops > k:
                continue
            for next_price, next_dest in adj[airport]:
                heapq.heappush(frontier, (cost + next_price, next_dest, stops + 1))

        return -1