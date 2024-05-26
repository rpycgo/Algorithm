import math

def solution(S: int) -> int:
    return (-1 + math.sqrt(1+4*2*S)) // 2


if __name__ == '__main__':
    S = int(input())
    print(solution(S))
