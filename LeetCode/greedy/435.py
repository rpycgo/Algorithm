class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort(key=lambda x: x[1])

        del_count = 0
        _, prev_end = intervals[0]

        for start, end in intervals[1:]:
            if prev_end > start:
                del_count += 1
            else:
                prev_end = end

        return del_count
