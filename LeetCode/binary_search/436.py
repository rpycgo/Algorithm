class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        starts = sorted((intervals[i][0], i) for i in range(n))
        start_vals = [start for start, _ in starts]

        answer = [-1] * n

        for i, (_, end) in enumerate(intervals):
            idx = bisect_left(start_vals, end)

            if idx < n:
                answer[i] = starts[idx][1]

        return answer
