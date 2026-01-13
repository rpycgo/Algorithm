import sys
from bisect import bisect_right


def get_primes(limit):
    is_prime = [True] * (limit+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]

    return is_prime, primes


def main():
    input = sys.stdin.readline

    MAX_VAL = 1299709
    is_prime_map, primes = get_primes(MAX_VAL)

    T = int(input())
    for _ in range(T):
        k = int(input())

        if is_prime_map[k]:
            print(0)
            continue

        idx = bisect_right(primes, k)
        answer = primes[idx] - primes[idx-1]

        print(answer)


if __name__ == '__main__':
    main()
