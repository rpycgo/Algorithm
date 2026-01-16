import sys
from collections import deque


input = sys.stdin.readline


def is_reachable(limit_fuel, points, N, k):
    limit_dist = (limit_fuel * 10) ** 2

    visited = [False] * (N + 2)
    visited[0] = True

    queue = deque([(0, 0)])
    while queue:
        curr_idx, count = queue.popleft()

        if count > k:
            continue

        curr_x, curr_y = points[curr_idx]
        dist_to_end = (10000 - curr_x)**2 + (10000 - curr_y)**2

        if dist_to_end <= limit_dist:
            return True

        if count == k:
            continue

        for next_idx in range(1, N+1):
            if not visited[next_idx]:
                nx, ny = points[next_idx]
                dist_sq = (curr_x - nx)**2 + (curr_y - ny)**2

                if dist_sq <= limit_dist:
                    visited[next_idx] = True
                    queue.append((next_idx, count+1))

    return False


def main():
    n, k = map(int, input().split())
    stations = [(0, 0)]
    stations.extend([tuple(map(int, input().split())) for _ in range(n)])
    stations.append((10000, 10000))

    left = 1
    right = 1500

    answer = right
    while left <= right:
        mid = (left + right) // 2

        if is_reachable(mid, stations, n, k):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
