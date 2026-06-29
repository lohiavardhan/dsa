class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_mat = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj_mat[n1].append(n2)
            adj_mat[n2].append(n1)
        
        visited = set()
        print(adj_mat)
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj_mat[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        

        return dfs(0, -1) and len(visited) == n