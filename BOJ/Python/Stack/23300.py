import sys


input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())

    backward = []
    forward = []
    curr = None

    cmds = []
    for _ in range(Q):
        query = input().split()
        cmd = query[0]

        if cmd == 'B':
            if backward:
                forward.append(curr)
                curr = backward.pop()
        elif cmd == 'F':
            if forward:
                backward.append(curr)
                curr = forward.pop()
        elif cmd == 'A':
            forward = []
            if curr is not None:
                backward.append(curr)

            curr = query[1]
        elif cmd == 'C':
            temp_backward = []

            if backward:
                temp_backward.append(backward[0])

                for i in range(1, len(backward)):
                    if backward[i] != backward[i-1]:
                        temp_backward.append(backward[i])

            backward = temp_backward


    answer_backward = [-1] if not backward else backward[::-1]
    answer_forward = [-1] if not forward else forward[::-1]

    print(curr)
    print(*answer_backward)
    print(*answer_forward)


if __name__ == '__main__':
    main()
