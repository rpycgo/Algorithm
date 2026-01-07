import sys


def update(tree, node, start, end, target, diff):
    if target < start or target > end:
        return

    tree[node] += diff

    if start != end:
        mid = (start+end) // 2
        update(tree, node*2, start, mid, target, diff)
        update(tree, node*2+1, mid+1, end, target, diff)


def query(tree, node, start, end, rank):
    if start == end:
        return start

    mid = (start+end) // 2

    n_left = tree[node*2]

    if rank <= n_left:
        return query(tree, node*2, start, mid, rank)
    else:
        return query(tree, node*2+1, mid+1, end, rank-n_left)


def main():
    input = sys.stdin.readline

    n = int(input())
    MAX_TASTES = 1_000_000

    tree = [0] * (MAX_TASTES*4)

    for _ in range(n):
        line = list(map(int, input().split()))

        if line[0] == 1:
            target_rank = line[1]
            taste = query(tree, 1, 1, MAX_TASTES, target_rank)

            print(taste)

            update(tree, 1, 1, MAX_TASTES, taste, -1)
        else:
            taste, diff = line[1], line[2]
            update(tree, 1, 1, MAX_TASTES, taste, diff)


if __name__ == '__main__':
    main()
