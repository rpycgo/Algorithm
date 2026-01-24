import sys


input = sys.stdin.readline


def main():
    N = int(input())
    for _ in range(N):
        case = input().rstrip()

        if not case:
            print(1)
            continue

        max_depth = 0
        curr_depth = 0

        for char in case:
            if char == '[':
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            else:
                curr_depth -=1

        answer = 2**max_depth
        print(answer)


if __name__ == '__main__':
    main()
