class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        answer = 0

        while left <= right:
            mid = (left+right) // 2

            if mid * mid <= num:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        if answer*answer == num:
            return True
        else:
            return False
