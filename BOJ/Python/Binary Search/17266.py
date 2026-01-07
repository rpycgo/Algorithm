import sys


def is_full_covered(height, positions, N):
    if positions[0] - height > 0:
        return False

    last_illuminated = positions[0] + height
    for i in range(1, len(positions)):
        current_start = positions[i] - height

        if current_start > last_illuminated:
            return False

        last_illuminated = positions[i] + height

    if last_illuminated < N:
        return False

    return True


def main():
    input = sys.stdin.readline

    N = int(input())
    M = int(input())
    street_lamp_positions = list(map(int, input().split()))

    left = 1
    right = N

    answer = right
    while left <= right:
        mid = (left+right) // 2

        if is_full_covered(mid, street_lamp_positions, N):
            answer = mid
            right = mid -1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
