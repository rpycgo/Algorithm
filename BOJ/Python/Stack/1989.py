import sys


input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split())) + [0]

    prefix_sum = [0] * (N+1)
    for i in range(N):
        prefix_sum[i+1] = prefix_sum[i] + A[i]

    max_score = -1
    result_range = (1, 1)
    stack = []

    for i, a in enumerate(A):
        while stack and a <= A[stack[-1]]:
            target_idx = stack.pop()
            height = A[target_idx]

            left = stack[-1] + 1 if stack else 0
            right = i - 1

            curr_sum = prefix_sum[right+1] - prefix_sum[left]
            curr_score = height * curr_sum

            if max_score < curr_score:
                max_score = curr_score
                result_range = (left+1, right+1)

        stack.append(i)

    print(max_score)
    print(f'{result_range[0]} {result_range[1]}')


if __name__ == '__main__':
    main()
