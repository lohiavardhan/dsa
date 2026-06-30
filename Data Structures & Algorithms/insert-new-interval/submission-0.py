class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        left = right = -1
        last = 0

        res = []

        for interval in intervals:
            if left == -1 and right == -1 and newInterval[0] > last and newInterval[1] < interval[0]:
                res.append(newInterval)
                res.append(interval)
                continue
            elif interval[1] < newInterval[0] or interval[0] > newInterval[1]:
                last = interval[1]
                res.append(interval)
                continue
            
            
            

            if left == -1 and interval[0] < newInterval[0] < interval[1]:
                left = interval[0]
            if right == -1 and interval[0] < newInterval[1] < interval[1]:
                right = interval[1]
            if left != -1 and right != -1:
                res.append([left, right])
        
        return res
            

            