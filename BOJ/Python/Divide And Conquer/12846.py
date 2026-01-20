import sys


input = sys.stdin.readline


class ScaryParTime:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr

    def find_max_salary(self, left, right):
        if left == right:
            return self.arr[left]

        mid = (left + right) // 2
        left_wage = self.find_max_salary(left, mid)
        right_wage = self.find_max_salary(mid+1, right)
        max_wage = max(left_wage, right_wage)

        low = mid
        high = mid + 1

        min_wage = min(self.arr[low], self.arr[high])
        max_wage = max(max_wage, min_wage*2)

        while left < low and high < right:
            if high < right and (low == left or self.arr[low - 1] < self.arr[high + 1]):
                high += 1
                min_wage = min(min_wage, self.arr[high])
            else:
                low -= 1
                min_wage = min(min_wage, self.arr[low])

            max_wage = max(max_wage, min_wage*(high-low+1))

        return max_wage

    def run(self):
        answer = self.find_max_salary(0, self.n-1)
        print(answer)


if __name__ == '__main__':
    n = int(input())
    daily_wages = tuple(map(int, input().split()))

    scary_part_time = ScaryParTime(n, daily_wages)
    scary_part_time.run()
