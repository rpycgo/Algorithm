class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def binary_search(target):
            left = 0
            right = int(sqrt(c))

            while left <= right:
                mid = (left+right) // 2
                val = mid * mid

                if val == target:
                    return True
                elif val < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False

        sqrt_c = int(sqrt(c))
        for a in range(sqrt_c+1):
            remain = c - a*a

            if binary_search(remain):
                return True

        return False
