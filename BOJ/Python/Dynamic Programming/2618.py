import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline


class PoliceCar:
    def __init__(self, N, W):
        self.N = N
        self.W = W

        self.events = [0] + [tuple(map(int, input().split())) for _ in range(W)]
        self.dp = [[-1] * (W+1) for _ in range(W+1)]

    def calculate_dist(self, p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    def backtrack(self, p1, p2):
        next_event = max(p1, p2) + 1

        if next_event > self.W:
            return

        target_pos = self.events[next_event]

        car1_pos = self.events[p1] if p1 != 0 else (1, 1)
        car2_pos = self.events[p2] if p2 != 0 else (self.N, self.N)

        car1_cost = self.calculate_dist(car1_pos, target_pos) + self.dp[next_event][p2]
        car2_cost = self.calculate_dist(car2_pos, target_pos) + self.dp[p1][next_event]

        if car1_cost < car2_cost:
            print(1)
            self.backtrack(next_event, p2)
        else:
            print(2)
            self.backtrack(p1, next_event)

    def solve(self, p1, p2):
        next_event = max(p1, p2) + 1

        if next_event > self.W:
            return 0

        if self.dp[p1][p2] != -1:
            return self.dp[p1][p2]

        target_pos = self.events[next_event]

        car1_pos = self.events[p1] if p1 != 0 else (1, 1)
        car1_dist = self.solve(next_event, p2) + self.calculate_dist(car1_pos, target_pos)

        car2_pos = self.events[p2] if p2 != 0 else (self.N, self.N)
        car2_dist = self.solve(p1, next_event) + self.calculate_dist(car2_pos, target_pos)

        self.dp[p1][p2] = min(car1_dist, car2_dist)

        return self.dp[p1][p2]


def main():
    N = int(input())
    W = int(input())

    police_car = PoliceCar(N, W)

    print(police_car.solve(0, 0))
    police_car.backtrack(0, 0)


if __name__ == '__main__':
    main()
