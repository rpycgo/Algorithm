import sys
from bisect import bisect_left, bisect_right


def main():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    answer = 0
    for i in range(N - 2):
        target = -A[i]

        left = i + 1
        right = N - 1

        while left < right:
            current_sum = A[left] + A[right]

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                if A[left] == A[right]:
                    count = right - left + 1
                    answer += (count * (count-1)) // 2
                    break
                else:
                    l_count = 1
                    r_count = 1

                    while left + 1 < right and A[left] == A[left+1]:
                        l_count += 1
                        left += 1
                    while right - 1 > left and A[right] == A[right-1]:
                        r_count += 1
                        right -= 1

                    answer += (l_count*r_count)
                    left += 1
                    right -= 1

    print(answer)


if __name__ == '__main__':
    main()
