import sys


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

            left = 0
            right = n - 1
            found = False

            while left < right:
                curr_sum = lengths[left] + lengths[right]

                if curr_sum == x_nm:
                    print(f'yes {lengths[left]} {lengths[right]}')
                    found = True
                    break
                elif curr_sum < x_nm:
                    left += 1
                else:
                    right -= 1

            if not found:
                print('danger')
        except:
            break


if __name__ == '__main__':
    main()
    