import sys


input = sys.stdin.readline


def can_cover(size, max_row, n_papers, cols):
    if size < max_row:
        return False
    
    cnt = 0
    last_cover = -1

    for col in cols:
        if col > last_cover:
            cnt += 1
            last_cover = col + size - 1

    return cnt <= n_papers


def main():
    r, c = map(int, input().split())
    n_papers = int(input())
    n_wrongs = int(input())

    max_row = 0
    wrong_points = []
    for _ in range(n_wrongs):
        r, c = map(int, input().split())
        wrong_points.append((r, c))

        if r > max_row:
            max_row = r

    wrong_points.sort(key=lambda x: x[1])
    cols = [wrong_point[1] for wrong_point in wrong_points]

    left = max_row
    right = 1_000_000
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if can_cover(mid, max_row, n_papers, cols):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
