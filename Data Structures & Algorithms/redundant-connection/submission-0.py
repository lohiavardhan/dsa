class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = set()
        for n1, n2 in edges:
            if n1 not in n:
                n.add(n1)
            if n2 not in n:
                n.add(n2)

        print(n)
        parent = [i for i in range(len(n) + 1)]
        rank = [1 for _ in range(len(n) + 1)]

        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]