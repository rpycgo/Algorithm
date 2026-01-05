class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left+right) // 2

            total_time = 0
            for pile in piles:
                total_time += (pile+mid-1) // mid

            if total_time <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left
