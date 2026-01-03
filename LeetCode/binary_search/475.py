class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        answer = 0
        for house in houses:
            idx = bisect_left(heaters, house)

            dist = float('inf')

            if idx < len(heaters):
                dist = abs(heaters[idx] - house)

            if idx > 0:
                dist = min(dist, abs(house-heaters[idx-1]))

            answer = max(answer, dist)

        return answer
