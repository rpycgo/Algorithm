import sys


input = sys.stdin.readline


def main():
    length, width, height = map(int, input().split())
    N = int(input())

    cubes = [0] * 20
    for _ in range(N):
        a, b = map(int, input().split())
        cubes[a] = b

    total_cnt = 0
    total_filled_vol = 0

    for i in range(19, -1, -1):
        total_filled_vol *= 8

        possible_cnt = (length // (2**i)) * (width // (2**i)) * (height // (2**i))
        add_cnt = possible_cnt - total_filled_vol
        actual_added = min(cubes[i], add_cnt)

        total_cnt += actual_added
        total_filled_vol += actual_added

    if total_filled_vol == length * width * height:
        print(total_cnt)
    else:
        print(-1)


if __name__ == '__main__':
    main()
