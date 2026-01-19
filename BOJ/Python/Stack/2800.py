import sys
from itertools import combinations


input = sys.stdin.readline


def main():
    expression = input().rstrip()

    stack = []
    pairs = []

    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            pairs.append((stack.pop(), i))

    results = set()
    for i in range(1, len(pairs)+1):
        for combination in combinations(pairs, i):
            remove_indices = set()

            for pair in combination:
                remove_indices.add(pair[0])
                remove_indices.add(pair[1])

            temp = ''
            for idx, char in enumerate(expression):
                if idx not in remove_indices:
                    temp += char

            results.add(temp)

    results = list(results)
    results.sort()
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
