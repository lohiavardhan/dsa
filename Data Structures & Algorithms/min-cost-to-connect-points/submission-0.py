class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        res = collections.defaultdict(int)

        for x, y in points:
            res[(x, y)] = float('inf')

        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                
                curr = abs(x1 - x2) + abs(y1 - y2)
                res[(x1, y1)] = min(res[(x1, y1)], curr)

        
        return sum(res.values()) - min(res.values())
