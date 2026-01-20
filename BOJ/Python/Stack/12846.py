import sys


input = sys.stdin.readline


class ScaryParTime:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr + [0]

    def find_max_salary(self):
        stack = []
        max_wages = 0

        for i, wage in enumerate(self.arr):
            while stack and self.arr[stack[-1]] >= wage:
                target_idx = stack.pop()
                height = self.arr[target_idx]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_wages = max(max_wages, height * width)

            stack.append(i)

        return max_wages

    def run(self):
        answer = self.find_max_salary()
        print(answer)


if __name__ == '__main__':
    n = int(input())
    daily_wages = list(map(int, input().split()))

    scary_part_time = ScaryParTime(n, daily_wages)
    scary_part_time.run()
