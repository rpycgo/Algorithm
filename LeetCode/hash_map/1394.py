from collections import defaultdict


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = defaultdict(int)
        answer = -1

        for num in arr:
            count[num] += 1

        for num, freq in count.items():
            if num == freq:
                answer = max(answer, num)

        return answer
