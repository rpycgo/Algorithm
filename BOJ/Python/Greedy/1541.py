def solution(string: str) -> int:
    string = string.split('-')

    total = 0
    for i, numbers in enumerate(string):
        numbers = numbers.split('+')
        _sum = 0
        for number in numbers:
            _sum += int(number)

        if i == 0:
            total += _sum
        else:
            total -= _sum

    return total


if __name__ == '__main__':
    string = input()
    print(solution(string))
