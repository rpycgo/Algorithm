import sys
import heapq

input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        energies = list(map(int, input().split()))

        heapq.heapify((energies))

        total_cost = 1
        while len(energies) > 1:
            slime_1 = heapq.heappop(energies)
            slime_2 = heapq.heappop(energies)

            new_slime = slime_1 * slime_2
            heapq.heappush(energies, new_slime)

            total_cost = (total_cost * new_slime) % 1_000_000_007

        answer = total_cost
        print(answer)


if __name__ == '__main__':
    main()
