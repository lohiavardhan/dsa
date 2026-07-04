"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted(interval.start for interval in intervals)
        end = sorted(interval.end for interval in intervals)

        count = 0
        res = 0

        i, j = 0, 0

        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                count += 1
                i += 1
            elif start[i] > end[j]:
                count -= 1
                j += 1
            else:
                i += 1
                j += 1
            
            res = max(res, count)
        
        return res