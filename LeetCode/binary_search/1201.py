class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = 1
        right = 2 * 10**9

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
        ab = self._lcm(a, b)
        bc = self._lcm(b, c)
        ac = self._lcm(a, c)
        abc = self._lcm(ab, c)

        return mid//a + mid//b + mid//c - mid//ab - mid//bc - mid//ac + mid//abc

    def _lcm(self, x, y):
        return (x * y) // gcd(x, y)
