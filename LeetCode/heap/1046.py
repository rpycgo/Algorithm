import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_heavy_weight = heapq.heappop(stones)
            second_heavy_weight = heapq.heappop(stones)

            if first_heavy_weight == second_heavy_weight:
                continue
            else:
                difference = first_heavy_weight - second_heavy_weight

                heapq.heappush(stones, difference)

        if len(stones) == 0:
            heapq.heappush(stones, 0)

        return -stones[0]
