"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) == 0:
            return 0
        
        intervals.sort(key= lambda x: x.end)
        i = 0
        res = 1
        new_res = 1

        # for interval in intervals:
        #     print(interval.start, interval.end)

        while i < len(intervals):
            j = i + 1
            higher = intervals[i].end
            while j < len(intervals) and higher > intervals[j].start:
                higher = max(higher, intervals[j].end)
                j += 1
                new_res += 1
            
            res = max(res, new_res)
            new_res = 1
            
            i = j

        return res 