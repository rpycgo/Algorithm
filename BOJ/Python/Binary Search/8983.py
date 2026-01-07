import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    M, N, L = map(int, input().split())

    shooting_stalls = list(map(int, input().split()))
    animal_coordinates = []
    for _ in range(N):
        animal_coordinate = list(map(int, input().split()))
        animal_coordinates.append(animal_coordinate)

    shooting_stalls.sort()

    answer = 0
    for x, y in animal_coordinates:
        if y > L:
            continue

        min_x = x - (L - y)
        max_x = x + (L - y)

        idx = bisect_left(shooting_stalls, min_x)

        if idx < M and shooting_stalls[idx] <= max_x:
            answer += 1

    print(answer)


if __name__ == '__main__':
    main()
