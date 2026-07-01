class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []
        count = 1
        i = 0
        intervals.sort()
        
        while i < len(intervals):
            
            for j in range(i + 1, len(intervals)):
                #print(intervals, i, j, intervals[i], intervals[j])
                if intervals[i][1] >= intervals[j][0]:
                    intervals[i][1] = intervals[j][1]
                    count += 1
            
                

            res.append(intervals[i])
            i += count if count != 0 else 1
            count = 1
        
        return res
                    

                    
