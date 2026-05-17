"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)

        intervals.sort(key=lambda x: x.start)
        total_rooms = []
        heapq.heappush(total_rooms, intervals[0].end)
        for i in range(1,len(intervals)):
            if intervals[i].start >= total_rooms[0]:
                heapq.heappop(total_rooms)
            heapq.heappush(total_rooms, intervals[i].end)
        
        return len(total_rooms)
