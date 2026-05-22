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
        if len(intervals) <= 1:
            return len(intervals)
        
        # we store only the end sorted by the smallest one in meanheap
        meeting_rooms = []
        intervals.sort(key=lambda x: x.start)
        heapq.heappush(meeting_rooms, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= meeting_rooms[0]:
                heapq.heappop(meeting_rooms)
            heapq.heappush(meeting_rooms, intervals[i].end)

        return len(meeting_rooms)