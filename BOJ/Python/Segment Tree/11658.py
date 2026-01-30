import sys


input = sys.stdin.readline
print = sys.stdout.write


class SegmentTree2D:
    def __init__(self, N, grid):
        self.N = N
        self.grid = grid

        self.h = (N-1).bit_length()
        self.size = 1 << self.h

        self.tree = [[0] * (2*self.size) for  _ in range(2*self.size)]

        self._build()

    def _build(self):
        for i in range(self.N):
            for j in range(self.N):
                self.tree[self.size+i][self.size+j] = self.grid[i][j]

        for i in range(self.size, 2*self.size):
            for j in range(self.size-1, 0, -1):
                self.tree[i][j] = self.tree[i][2*j] + self.tree[i][2*j + 1]

        for i in range(self.size-1, 0, -1):
            for j in range(1, 2*self.size):
                self.tree[i][j] = self.tree[2*i][j] + self.tree[2*i + 1][j]

    def _query_row(self, node, y1, y2):
        left = y1 + self.size
        right = y2 + self.size

        total = 0
        while left <= right:
            if left%2 == 1:
                total += self.tree[node][left]
                left += 1

            if right%2 == 0:
                total += self.tree[node][right]
                right -= 1

            left //= 2
            right //= 2

        return total

    def query(self, x1, y1, x2, y2):
        top = x1 + self.size
        bottom = x2 + self.size

        total = 0
        while top <= bottom:
            if top%2 == 1:
                total += self._query_row(top, y1,  y2)
                top += 1
            if bottom%2 == 0:
                total += self._query_row(bottom, y1, y2)
                bottom -= 1

            top //= 2
            bottom //= 2

        return total

    def update(self, x, y, val):
        x += self.size
        y += self.size

        self.tree[x][y] = val

        curr_y = y
        while curr_y > 1:
            curr_y //= 2
            self.tree[x][curr_y] = self.tree[x][2*curr_y] + self.tree[x][2*curr_y + 1]

        curr_x = x
        while curr_x > 1:
            curr_x //= 2

            temp_y = y
            self.tree[curr_x][temp_y] = self.tree[2*curr_x][temp_y] + self.tree[2*curr_x + 1][temp_y]

            while temp_y > 1:
                temp_y //= 2
                self.tree[curr_x][temp_y] = self.tree[2*curr_x][temp_y] + self.tree[2*curr_x + 1][temp_y]


def main():
    N, M = map(int, input().split())
    grid = [tuple(map(int, input().split())) for _ in range(N)]

    segment_tree = SegmentTree2D(N, grid)

    answer = []
    for _ in range(M):
        w, *cmd = tuple(map(int, input().split()))

        if w == 0:
            x, y, c = cmd
            segment_tree.update(x-1, y-1, c)
        else:
            x1, y1, x2, y2 = cmd
            result = segment_tree.query(x1-1, y1-1, x2-1, y2-1)

            answer.append(str(result))

    print('\n'.join(answer) + '\n')


if __name__ == '__main__':
    main()
