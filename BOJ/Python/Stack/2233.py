import sys


input = sys.stdin.readline


def main():
    N = int(input())
    binaries = input().rstrip()
    X, Y = map(int, input().split())

    idx_to_node = [0] * (2*N)
    parent = [0] * (N+1)
    depth = [0] * (N+1)
    node_range = [[0, 0] for _ in range(N+1)]

    stack = []
    node_cnt = 0

    for i, char in enumerate(binaries):
        if char == '0':
            node_cnt += 1

            if stack:
                parent[node_cnt] = stack[-1]
                depth[node_cnt] = depth[stack[-1]] + 1

            idx_to_node[i] = node_cnt
            node_range[node_cnt][0] = i + 1
            stack.append(node_cnt)
        else:
            curr = stack.pop()
            idx_to_node[i] = curr
            node_range[curr][1] = i + 1

    node_x = idx_to_node[X-1]
    node_y = idx_to_node[Y-1]

    while depth[node_x] > depth[node_y]:
        node_x = parent[node_x]
    while depth[node_y] > depth[node_x]:
        node_y = parent[node_y]

    while node_x != node_y:
        node_x = parent[node_x]
        node_y = parent[node_y]

    print(f'{node_range[node_x][0]} {node_range[node_x][1]}')


if __name__ == '__main__':
    main()
