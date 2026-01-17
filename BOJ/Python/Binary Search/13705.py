import sys
from decimal import Decimal, getcontext


input = sys.stdin.readline
getcontext().prec = 50


def decimal_sin(x):
    pi = Decimal('3.14159265358979323846264338327950288419716939937510')
    x = x % (Decimal('2') * pi)

    result = Decimal(0)
    term = x
    x_squared = x * x

    for i in range(1, 100):
        result += term

        term *= -x_squared / (Decimal(2*i) * Decimal(2*i + 1))

        if abs(term) < Decimal('1e-50'):
            break

    return result


def main():
    A, B, C = map(int, input().split())
    A, B, C = Decimal(A), Decimal(B), Decimal(C)

    left = (C - B) / A
    right = (C + B) / A

    for _ in range(100):
        mid = (left + right) / 2

        val = A*mid + B*decimal_sin(mid) - C

        if val > 0:
            right = mid
        else:
            left = mid

    print(f'{right:.6f}')


if __name__ == '__main__':
    main()
