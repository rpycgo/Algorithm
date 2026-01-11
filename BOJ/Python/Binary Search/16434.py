import sys


def is_survival(hp, h_atk, statuses):
    max_hp = hp

    for status in statuses:
        t, a, h = status

        if t == 1:
            cnt = (h + h_atk - 1) // h_atk

            total_damage = (cnt-1) * a

            hp -= total_damage

            if hp <= 0:
                return False

        elif t == 2:
            hp = min(hp+h, max_hp)
            h_atk += a

    return True


def main():
    input = sys.stdin.readline

    N, H_ATK = map(int, input().split())

    left = 1
    right = 123_456 * 1_000_000 * 1_000_000

    statuses = [list(map(int, input().split())) for _ in range(N)]

    answer = right
    while left <= right:
        mid = (left+right) // 2

        if is_survival(mid, H_ATK, statuses):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
