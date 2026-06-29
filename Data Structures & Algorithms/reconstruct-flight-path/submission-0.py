class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj_list = defaultdict(list)
        visited = defaultdict(int)

        for source, dest in tickets:
            adj_list[source].append(dest)
            visited[dest] += 1
        
        # visited["JFK"] += 1
        
        heap = []
        heapq.heappush(heap, "JFK")
        res = []

        print(adj_list, visited)
        
        while heap and len(res) < 100:
            
            next_dest = heapq.heappop(heap)
            res.append(next_dest)

            
            for dst in adj_list[next_dest]:
                if visited[dst] <= 0:
                    continue
                else:
                    visited[dst] -= 1
                    heapq.heappush(heap, dst)

            print(next_dest, visited, heap)


        return res