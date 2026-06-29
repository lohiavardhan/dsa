class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for source, destination, price in flights:
            adj[source].append((price, destination))
        
        frontier = [(0, flights[0][0], 0)]

        while frontier:
            print(frontier)
            cost, airport, stops = heapq.heappop(frontier)

            if airport == dst:
                return cost
            if stops > k:
                continue
            
            for np, na in adj[airport]:
                heapq.heappush(frontier, (cost + np, na, stops + 1))
        
        return -1
