class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        removed = 0
        current_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < current_end:
                removed += 1
            else:
                current_end = end
                
        return removed