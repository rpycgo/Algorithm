import sys


input = sys.stdin.readline


def main():
    R, C = map(int, input().split())
    table = [input().rstrip() for _ in range(R)]

    col_strings = []
    for j in range(C):
        col_str = ''.join(table[i][j] for i in range(R))
        col_strings.append(col_str)

    left = 0
    right = R - 1
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if mid == 0:
            left = mid + 1
            continue

        exists = set()
        is_unique = True

        for j in range(C):
            string_part = col_strings[j][mid:]

            if string_part in exists:
                is_unique = False
                break

            exists.add(string_part)

        if is_unique:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


if __name__ == '__main__':
    main()
