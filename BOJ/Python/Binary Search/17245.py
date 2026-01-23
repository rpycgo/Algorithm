import sys


input = sys.stdin.readline


def check_cooled_servers(height, servers):
    n_cooled_servers = 0
    for server in servers:
        if server > height:
            n_cooled_servers += height
        else:
            n_cooled_servers += server

    return n_cooled_servers


def main():
    N = int(input())

    total_servers = 0
    max_height = 0

    servers = []
    for _ in range(N):
        row = tuple(map(int, input().split()))

        for server in row:
            if server > 0:
                servers.append(server)
                total_servers += server

                if server > max_height:
                    max_height = server

    if total_servers == 0:
        print(0)
        return

    target = (total_servers + 1) // 2

    left = 0
    right = max_height
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if check_cooled_servers(mid, servers) >= target:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
