def main():
    n = int(input())

    left = 1
    right = n

    answer = right
    while left <= right:
        mid = (left+right) // 2

        if mid*mid >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
