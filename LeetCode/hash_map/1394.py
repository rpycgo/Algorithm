from collections import defaultdict


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = defaultdict(int)
        candidates = []

        for num in arr:
            count[num] += 1

        for _, num in enumerate(arr):
            if count[num] == num:
                candidates.append(num)

        answer = max(candidates) if candidates else -1

        return answer
