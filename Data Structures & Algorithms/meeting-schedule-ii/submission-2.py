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

        while i < len(intervals):
            j = i + 1
            while j < len(intervals) and intervals[i].end > intervals[j].start:
                j += 1
                new_res += 1
            
            res = max(res, new_res)
            new_res = 1
            
            i = j

        return res 