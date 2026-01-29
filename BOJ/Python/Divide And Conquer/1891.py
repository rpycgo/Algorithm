import sys


input = sys.stdin.readline


class Quadrant:
    def __init__(self, d, num):
        self.d = d
        self.num = num

        self.size = 1 << d
        self.x, self.y = self._to_coordinate()

    def _to_coordinate(self):
        curr_x, curr_y = 0, 0
        temp_size = self.size

        for char in str(self.num):
            temp_size //= 2

            if char == '1':
                curr_x += temp_size
            elif char == '2':
                pass
            elif char == '3':
                curr_y += temp_size
            elif char == '4':
                curr_x += temp_size
                curr_y += temp_size

        return curr_x, curr_y

    def move(self, x, y):
        self.x += x
        self.y -= y

        if 0 <= self.x < self.size and 0 <= self.y < self.size:
            return True

        return False

    def to_quadrant(self):
        results = []
        curr_x, curr_y = self.x, self.y
        temp_size = self.size

        for _ in range(self.d):
            temp_size //= 2

            if curr_x < temp_size and curr_y < temp_size:
                results.append('2')
            elif curr_x >= temp_size and curr_y < temp_size:
                results.append('1')

                curr_x -= temp_size
            elif curr_x < temp_size and curr_y >= temp_size:
                results.append('3')

                curr_y -= temp_size
            else:
                results.append('4')

                curr_x -= temp_size
                curr_y -= temp_size

        return ''.join(results)


def main():
    d, num = map(int, input().split())
    x, y = map(int, input().split())

    quadrant = Quadrant(d, num)

    answer = quadrant.to_quadrant() if quadrant.move(x, y) else -1
    print(answer)


if __name__ == '__main__':
    main()
