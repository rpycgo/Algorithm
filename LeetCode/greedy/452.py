class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        points.sort(key=lambda x: x[1])

        min_count = 1
        _, prev_end = points[0]

        for start, end in points[1:]:
            if prev_end < start:
                min_count += 1
                prev_end = end

        return min_count
