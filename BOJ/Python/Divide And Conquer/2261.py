import sys


input = sys.stdin.readline


class ClosestPairPoints:
    def __init__(self, n, points):
        self.n = n
        self.points = sorted(points)

    def _calculate_dist(self, p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    def find(self, start, end):
        if end - start + 1 <= 3:
            min_dist = float('inf')

            for i in range(start, end):
                for j in range(i+1, end+1):
                    min_dist = min(min_dist, self._calculate_dist(self.points[i], self.points[j]))

            return min_dist

        mid = (start+end) // 2
        mid_x = self.points[mid][0]

        left_dist = self.find(start, mid)
        right_dist = self.find(mid+1, end)
        dist = min(left_dist, right_dist)

        filtering = [
            self.points[i]
            for i
            in range(start, end+1)
            if (self.points[i][0] - mid_x) ** 2 < dist
        ]
        filtering.sort(key=lambda x: x[1])

        for i in range(len(filtering)):
            for j in range(i+1, len(filtering)):
                if (filtering[i][1] - filtering[j][1])**2 >= dist:
                    break
                
                curr_dist = self._calculate_dist(filtering[i], filtering[j])
                dist = min(dist, curr_dist)

        return dist

    def run(self):
        result = self.find(0, self.n-1)
        print(result)


if __name__ == '__main__':
    n = int(input())
    points = [
        tuple(map(int, input().split()))
        for _
        in range(n)
    ]

    closest_pair_points = ClosestPairPoints(n, points)
    closest_pair_points.run()
