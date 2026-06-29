class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_graph = defaultdict(list)

        for ui, vi, ti in times:
            adj_graph[ui].append([vi, ti])
    
        visited = set()
        res = float("inf")
        
        def dfs(curr, times):
            nonlocal res
            if curr in visited:
                return
            
            visited.add(curr)
            if len(visited) == n:
                res = min(res, times)
                return

            for vi, ti in adj_graph[curr]:
                times += ti
                dfs(vi, times)
                times -= ti

            visited.remove(curr)
            

        
        dfs(k, 0)

        return res if res != float("inf") else -1