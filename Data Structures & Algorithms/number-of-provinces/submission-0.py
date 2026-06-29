class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS = len(isConnected)
        provinces = ROWS
        parent = [i for i in range(ROWS)]
        rank = [1 for _ in range(ROWS)]

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
        
        for i in range(ROWS):
            for j in range(i + 1, ROWS):
                if i == j:
                    continue
                
                if isConnected[i][j] == 1:
                    provinces -= union(i, j)


        return provinces