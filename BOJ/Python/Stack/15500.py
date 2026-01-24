import sys


input = sys.stdin.readline


def main():
    K = int(input())
    pillar1 = list(map(int, input().split()))

    pillar2 = []
    pos = [0] * (K+1)
    for num in pillar1:
        pos[num] = 1

    moves = []
    target = K

    while target > 0:
        if pos[target] == 1:
            while pillar1[-1] != target:
                top = pillar1.pop()
                pillar2.append(top)
                pos[top] = 2
                moves.append('1 2')

            pillar1.pop()
            moves.append('1 3')
            target -= 1
        else:
            while pillar2[-1] != target:
                top = pillar2.pop()
                pillar1.append(top)
                pos[top] = 1
                moves.append('2 1')

            pillar2.pop()
            moves.append('2 3')
            target -= 1

    print(len(moves))
    print('\n'.join(moves))


if __name__ == '__main__':
    main()
