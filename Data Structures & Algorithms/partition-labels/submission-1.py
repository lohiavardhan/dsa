class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_occ = {}
        for i, char in enumerate(s):
            last_occ[char] = i
        
        res = []
        count = end = 0

        for i, char in enumerate(s):
            count += 1
            end = max(end, last_occ[char])

            if i == end:
                res.append(count)
                count = 0
        
        return res