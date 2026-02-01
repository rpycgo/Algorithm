import sys


input = sys.stdin.readline


class StoneThrowing:
    def __init__(self, R, C, board):
        self.R = R
        self.C = C
        self.board = board

        self.path_stacks = [[] for _ in range(C)]

    def find_final_pos(self, start):
        while self.path_stacks[start]:
            r, c = self.path_stacks[start][-1]

            if self.board[r][c] != '.':
                self.path_stacks[start].pop()
            else:
                break

        if not self.path_stacks[start]:
            curr_r, curr_c = 0, start
        else:
            curr_r, curr_c = self.path_stacks[start][-1]

        while True:
            self.path_stacks[start].append((curr_r, curr_c))

            if curr_r+1 == self.R or self.board[curr_r+1][curr_c] == 'X':
                break

            elif self.board[curr_r+1][curr_c] == 'O':
                if curr_c > 0 and self.board[curr_r][curr_c-1] == '.' and \
                    self.board[curr_r+1][curr_c-1] == '.':
                    curr_r += 1
                    curr_c -= 1
                elif curr_c < self.C-1 and self.board[curr_r][curr_c+1] == '.' and \
                    self.board[curr_r+1][curr_c+1] == '.':
                    curr_r += 1
                    curr_c += 1
                else:
                    break
            else:
                curr_r += 1

        self.board[curr_r][curr_c] = 'O'


def main():
    R, C = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(R)]

    stone_throwing = StoneThrowing(R, C, board)

    N = int(input())
    for _ in range(N):
        query = int(input())
        stone_throwing.find_final_pos(query-1)

    for row in stone_throwing.board:
        print(''.join(row))


if __name__ == '__main__':
    main()
