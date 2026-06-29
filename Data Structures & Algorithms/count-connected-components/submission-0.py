class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adjacency[n1].append(n2)
        
        visited = set()

        def dfs(node):
            visited.add(node)
            for nei in adjacency[node]:
                dfs(nei)
            
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res
