class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calculate_days(max_weight):
            days = 1

            total_weight = 0
            for weight in weights:
                if total_weight+weight <= max_weight:
                    total_weight += weight
                else:
                    days += 1
                    total_weight = weight

            return days

        left = max(weights)
        right = sum(weights)

        answer = right
        while left <= right:
            mid = (left+right) // 2

            if calculate_days(mid) <= days:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
