class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = 1
        right = a * b * c

        answer = right
        while left <= right:
            mid = (left+right) // 2

            if self.get_n_ugly_number(mid, a, b, c) >= n:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

    def get_n_ugly_number(self, mid, a, b, c):
        count = 0
        for i in range(1, mid+1):
            if i%a == 0 or i%b == 0 or i%c == 0:
                count += 1

        return count
