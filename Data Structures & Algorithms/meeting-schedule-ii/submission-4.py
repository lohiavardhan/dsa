"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key= lambda x: x.start)
        rooms = 1
        i = 0

        while i < len(intervals):
            curr = 1
            while i + 1 < len(intervals) and intervals[i].end > intervals[i + 1].start:
                curr += 1
                i += 1
                rooms = max(rooms, curr)
            
            i += 1
        
        return rooms