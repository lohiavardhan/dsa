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
        print([[interval.start, interval.end] for interval in intervals])
        rooms = 1
        i = 0

        while i < len(intervals):
            curr = 1
            min_end = float('inf')
            while i + 1 < len(intervals) and intervals[i].end > intervals[i + 1].start and (intervals[i + 1].start > min_end or min_end == float('inf')):
                min_end = min(min_end, intervals[i].end)
                curr += 1
                i += 1
                rooms = max(rooms, curr)
            
            i += 1
        
        return rooms