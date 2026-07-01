class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []
        i = 0
        intervals.sort()
        
        while i < len(intervals):

            j = i + 1
            while j < len(intervals) and intervals[i][1] >= intervals[j][0]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                intervals[i][0] = min(intervals[j][0], intervals[i][0])
                j += 1

            res.append(intervals[i])
            i = j
        
        return res
                    

                    
