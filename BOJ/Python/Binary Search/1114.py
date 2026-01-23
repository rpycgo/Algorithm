import sys


input = sys.stdin.readline


def can_cut(limit, C, dists):
    cnt = 0
    curr_len = 0

    for i in range(len(dists)-1, -1, -1):
        if dists[i] > limit:
            return None, None

        if curr_len + dists[i] > limit:
            cnt += 1
            curr_len = dists[i]
        else:
            curr_len += dists[i]

    first_cut = dists[0] if cnt < C else curr_len

    if cnt > C:
        return None, None

    return cnt, first_cut


def main():
    L, K, C = map(int, input().split())

    cut_pos = list(map(int, input().split()))
    cut_pos.sort()

    points = [0] + cut_pos + [L]
    dists = [points[i+1] - points[i] for i in range(len(points)-1)]

    if max(dists) > L:
        pass

    left, right = max(dists), L

    answer_pos = right
    answer_first = 0

    while left <= right:
        mid = (left + right) // 2

        cnt, first_cut = can_cut(mid, C, dists)

        if cnt is not None:
            answer_pos = mid
            answer_first = first_cut

            right = mid - 1
        else:
            left = mid + 1

    print(f'{answer_pos} {answer_first}')


if __name__ == '__main__':
    main()
