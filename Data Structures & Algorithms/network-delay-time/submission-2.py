class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_graph = defaultdict(list)

        for ui, vi, ti in times:
            adj_graph[ui].append([vi, ti])
    
        heap = []
        heapq.heappush(heap, (0, k))
        res = [float("inf") for _ in range(n)] 
        
        while heap:
            curr_time, curr_val = heapq.heappop(heap)
            res[curr_val - 1] = min(res[curr_val - 1], curr_time)

            for vi, ti in adj_graph[curr_val]:
                heapq.heappush(heap, [ti + res[curr_val - 1], vi])
            
        answer = max(res)
        if answer == float("inf"):
            return -1
        
        return answer