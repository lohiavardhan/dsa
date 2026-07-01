class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        res = 0

        i = 0

        #print(intervals)

        while i < len(intervals):

            j = i + 1
            while j < len(intervals) and intervals[i][1] > intervals[j][0]:
                j += 1
                res += 1

            i = j
        
        return res
                