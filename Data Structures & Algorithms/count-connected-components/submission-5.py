class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n + 1)]
        rank = [1 for _ in range(n + 1)]

        def search(n):
            res = n
            while res != parent[n]:
                parent[n] = parent[parent[n]]
                res = parent[n]
            
            return res
        
        def union(n1, n2):
            p1, p2 = search(n1), search(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return 1
        
        res = n

        for u, v in edges:
            res -= union(u, v)
        
        return res
