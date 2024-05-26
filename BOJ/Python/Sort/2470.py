def solution(solution: list[int]) -> list[int]:
    solution.sort()

    start_index = 0
    last_index = len(solution)-1
    minimum = 9999999999999
    array = [0, 0]

    while start_index < last_index:
        _sum = solution[start_index] + solution[last_index]   

        if abs(_sum) < abs(minimum):
            minimum = _sum
            array[0], array[1] = solution[start_index], solution[last_index]

        if _sum >= 0:
            last_index -= 1
        else:
            start_index +=1

    return array


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))

    for number in solution(numbers):
        print(number, end=' ', sep='')
