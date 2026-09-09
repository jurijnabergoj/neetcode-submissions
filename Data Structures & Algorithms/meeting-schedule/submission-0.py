"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intrs = sorted(intervals, key=lambda x: x.start)
        for i in range(len(intervals) - 1):
            if intrs[i].end > intrs[i + 1].start:
                return False
        return True