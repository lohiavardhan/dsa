class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adjacency[n1].append(n2)
            adjacency[n2].append(n1)
        
        visited = set()

        def dfs(node, prev):
            
            visited.add(node)
            print(node, visited)
            for nei in adjacency[node]:
                if nei == prev:
                    continue
                dfs(nei, node)
            
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i, -1)
        
        return res
