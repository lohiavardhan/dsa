class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_mat = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj_mat[n1].append(n2)
        
        def dfs(node, visited):
            print(node, adj_mat[node], visited)
            if node in visited:
                return False
            
            visited.add(node)
            for next in adj_mat[node]:
                if not dfs(next, visited):
                    return False
            return True
        
        for i in range(n):
            if not dfs(i, set()):
                return False
            

        return True