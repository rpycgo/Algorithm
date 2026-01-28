import sys


input = sys.stdin.readline


def main():
    N = int(input())
    seqs = tuple(map(int, input().split()))

    top_stacks = [0, 0, 0, 0]
    for num in seqs:
        is_placed = False

        for i in range(4):
            if top_stacks[i] < num:
                top_stacks[i] = num
                is_placed = True
                break

        if not is_placed:
            print('NO')
            return

    print('YES')


if __name__ == '__main__':
    main()
