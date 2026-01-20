import sys


input = sys.stdin.readline


def binary_search(key, n):
    left, right = 0, n - 1

    cnt = 0
    while left <= right:
        mid = (left + right) // 2

        if key == mid:
            break
        elif key < mid:
            right = mid - 1
        else:
            left = mid + 1

        cnt += 1

    return cnt


def ternary_search(key, n):
    left, right = 0, n - 1
    cnt = 0

    while left <= right:
        p1 = left + (right - left) // 3
        p2 = right - (right - left) // 3

        if key == p1:
            break
        else:
            cnt += 1

            if key == p2:
                break
            else:
                cnt += 1

                if key < p1:
                    right = p1 - 1
                elif key < p2:
                    left = p1 + 1
                    right = p2 - 1
                else:
                    left = p2 + 1
    return cnt


def main():
    N = int(input())

    n_less, n_equal, n_greater = 0, 0, 0
    for i in range(N):
        cnt_binary = binary_search(i, N)
        cnt_ternary = ternary_search(i, N)

        if cnt_binary < cnt_ternary:
            n_less += 1
        elif cnt_binary == cnt_ternary:
            n_equal += 1
        else:
            n_greater += 1

    print(n_less)
    print(n_equal)
    print(n_greater)


if __name__ == '__main__':
    main()
