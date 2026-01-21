import sys


input = sys.stdin.readline


def main():
    N, L = map(int, input().split())
    leak_coords = list(map(int, input().split()))

    leak_coords.sort()

    cnt = 0
    last_covered = 0

    for leak_coord in leak_coords:
        if leak_coord > last_covered:
            cnt += 1

            last_covered = leak_coord + L - 0.5

    print(cnt)


if __name__ == '__main__':
    main()
