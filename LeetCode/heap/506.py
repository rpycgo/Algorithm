import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(heap)

        result = [""] * len(score)
        rank = 1

        while heap:
            _, idx = heapq.heappop(heap)
            if rank == 1:
                result[idx] = "Gold Medal"
            elif rank == 2:
                result[idx] = "Silver Medal"
            elif rank == 3:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank)

            rank += 1

        return result
