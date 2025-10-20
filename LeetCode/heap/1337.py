import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sums = [(sum(row), i) for i, row in enumerate(mat)]
        heapq.heapify(sums)

        top_k = heapq.nsmallest(k, sums)

        return [i for _, i in top_k]
