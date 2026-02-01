import sys


input = sys.stdin.readline


def main():
    N = int(input())

    min_y = float('inf')
    start_idx = -1
    boundaries = []

    for i in range(N):
        x, y = map(int, input().split())
        boundaries.append((x, y))

        if y < min_y:
            min_y = y
            start_idx = i

    boundaries = boundaries[start_idx:] + boundaries[:start_idx]
    boundaries.append(boundaries[0])

    segments = []
    temp_x = None

    for i in range(N):
        x1, y1 = boundaries[i]
        x2, y2 = boundaries[i+1]

        if x1 == x2:
            if y1 < 0 and y2 > 0:
                temp_x = x1
            elif y1 > 0 and y2 < 0:
                if temp_x is not None:
                    segments.append((min(temp_x, x1), max(temp_x, x1)))
                    temp_x = None

    segments.sort()

    outer_cnt = 0
    stack = []
    has_child = [False] * len(segments)

    last_end = float('-inf')
    for i, segment in enumerate(segments):
        curr_start, curr_end = segment

        if curr_start > last_end:
            outer_cnt += 1
            last_end = curr_end

        while stack and segments[stack[-1]][1] < curr_start:
            stack.pop()

        if stack:
            has_child[stack[-1]] = True

        stack.append(i)

    inner_cnt = 0
    for i in range(len(segments)):
        if i == len(segments)-1 or segments[i+1][0] > segments[i][1]:
            inner_cnt += 1

    print(f'{outer_cnt} {inner_cnt}')


if __name__ == '__main__':
    main()
