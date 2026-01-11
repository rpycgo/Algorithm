import sys
from bisect import bisect_left


def get_input():
    for line in sys.stdin:
        for word in line.split():
            yield word


def main():
    input_data = get_input()

    while True:
        try:
            x_str = next(input_data)
            x_nm = int(x_str)*10_000_000

            n_str = next(input_data)
            n = int(n_str)

            lengths = []
            for _ in range(n):
                length_str = next(input_data)
                length = int(length_str)
                lengths.append(length)
            lengths.sort()

            is_found = False
            for i, length in enumerate(lengths):
                target = x_nm - length

                idx = bisect_left(lengths, target, i+1)

                if idx < n and lengths[idx] == target:
                    print(f'yes {length} {target}')
                    is_found = True
                    break

            if not is_found:
                print('danger')
        except:
            break


if __name__ == '__main__':
    main()
