class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_mat = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj_mat[n1].append(n2)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)
            for next in adj_mat[node]:
                if not dfs(next):
                    return False
            return True
        

        return dfs(0) and len(visited) == n