class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)

        for source, dest, price in flights:
            adj[source].append((price, dest))
        
        frontier = []
        visited = set()

        heapq.heappush(frontier, (0, src, 0))
        while frontier:
            print(frontier)
            cost, airport, stops = heapq.heappop(frontier)
            print(cost, airport, stops)
            if airport == dest:
                return cost
            if airport in visited or stops > k:
                continue
            visited.add(airport)
            for next_price, next_dest in adj[airport]:
                if next_dest in visited:
                    continue
                heapq.heappush(frontier, (cost + next_price, next_dest, stops + 1))



        return -1