import sys
from bisect import bisect_left


def main():
    input = sys.stdin.read
    input_data = input().split()

    ptr = 0
    while ptr < len(input_data):
        x_nm = int(input_data[ptr]*10000000)
        ptr += 1

        n = int(input_data[ptr])
        ptr += 1

        lengths = []
        for _ in range(n):
            lengths.append(int(input_data[ptr]))
            ptr += 1
        lengths.sort()

        for length in lengths:
            target = x_nm-length
            idx = bisect_left(lengths, target)

            if idx < n and lengths[idx] == target:
                print(f'yes {length} {target}')
                break

        print('danger')


if __name__ == '__main__':
    main()
    